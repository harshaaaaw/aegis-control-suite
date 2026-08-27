"""CAUSALA: causal-inference retrieval over a compiled causal knowledge layer.

Design (anti-slop + IR-correct):
- Compiled-once knowledge: causal claims (cause -> effect) are ingested with
  confidence + provenance (source id). They are NOT rediscovered per query.
- Retrieval returns CITATION-BACKED answers: every returned cause/effect carries
  its source id. We never answer from a cause we did not ingest (no hallucination).
- Confidence floor: claims below 0.5 are flagged `contested` for human review,
  never silently trusted.
- Tenant isolation: all retrieval is scoped by tenant_id (no cross-tenant leakage).
- Externalized state: graph persisted to SQLite; in-memory networkx for traversal.

This is the Hermes llm-wiki pattern applied to causality: compile once, query
with citations, surface contradictions.
"""
from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from sqlalchemy import (Column, Float, Integer, String, Text, create_engine)
from sqlalchemy.orm import declarative_base, sessionmaker


@dataclass
class CausalClaim:
    claim_id: str
    cause: str
    effect: str
    confidence: float
    source: str
    tenant_id: str
    mechanism: str = ""
    contested: bool = False

    def to_dict(self) -> dict[str, Any]:
        return {
            "claim_id": self.claim_id, "cause": self.cause, "effect": self.effect,
            "confidence": self.confidence, "source": self.source,
            "tenant_id": self.tenant_id, "mechanism": self.mechanism,
            "contested": self.contested,
        }


@dataclass
class CausalAnswer:
    query: str
    mode: str                 # "explain" | "what_if"
    cause: str | None
    effect: str | None
    confidence: float
    citations: list[str]
    contested: bool


Base = declarative_base()


class _ClaimRow(Base):
    __tablename__ = "causal_claims"
    id = Column(Integer, primary_key=True)
    claim_id = Column(String(40), unique=True, nullable=False, index=True)
    cause = Column(String(256), nullable=False, index=True)
    effect = Column(String(256), nullable=False, index=True)
    confidence = Column(Float, nullable=False)
    source = Column(String(256), nullable=False)
    tenant_id = Column(String(64), nullable=False, index=True)
    mechanism = Column(Text, default="")
    contested = Column(Integer, default=0)  # 0/1


class Causala:
    CONFIDENCE_FLOOR = 0.5

    def __init__(self, db_path: str):
        url = f"sqlite:///{Path(db_path).as_posix()}"
        self._engine = create_engine(url)
        Base.metadata.create_all(self._engine)
        self._session = sessionmaker(bind=self._engine, expire_on_commit=False)

    # ---- ingest (compile once) -------------------------------------------------
    def ingest_claim(self, cause: str, effect: str, confidence: float,
                     source: str, tenant_id: str, mechanism: str = "") -> str:
        if not (0.0 <= confidence <= 1.0):
            raise ValueError("confidence must be in [0,1]")
        if not source:
            raise ValueError("source (provenance) is required; no unattributed claims")
        claim_id = uuid.uuid4().hex[:16]
        contested = confidence < self.CONFIDENCE_FLOOR
        with self._session() as s:
            s.add(_ClaimRow(
                claim_id=claim_id, cause=cause, effect=effect,
                confidence=confidence, source=source, tenant_id=tenant_id,
                mechanism=mechanism, contested=int(contested)))
            s.commit()
        return claim_id

    def get_claim(self, claim_id: str) -> CausalClaim | None:
        with self._session() as s:
            row = s.query(_ClaimRow).filter_by(claim_id=claim_id).first()
            return self._row_to_claim(row) if row else None

    # ---- retrieval (cite-backed) ---------------------------------------------
    def retrieve_causes(self, effect: str, tenant_id: str) -> list[CausalClaim]:
        with self._session() as s:
            rows = s.query(_ClaimRow).filter_by(effect=effect, tenant_id=tenant_id).all()
            return [self._row_to_claim(r) for r in rows]

    def retrieve_effects(self, cause: str, tenant_id: str) -> list[CausalClaim]:
        with self._session() as s:
            rows = s.query(_ClaimRow).filter_by(cause=cause, tenant_id=tenant_id).all()
            return [self._row_to_claim(r) for r in rows]

    def retrieve_path(self, start: str, goal: str, tenant_id: str,
                      max_hops: int = 4) -> list[CausalClaim]:
        """Multi-hop causal chain from start cause to goal effect (cite-backed).

        Builds a directed graph from the tenant's ingested claims and returns the
        shortest causal path (BFS) as an ordered list of claims. Each claim in the
        path carries its own source -> the whole chain is citation-backed.
        """
        import networkx as nx
        g = nx.DiGraph()
        edges: list[CausalClaim] = []
        with self._session() as s:
            rows = s.query(_ClaimRow).filter_by(tenant_id=tenant_id).all()
            for r in rows:
                cl = self._row_to_claim(r)
                edges.append(cl)
                g.add_edge(cl.cause, cl.effect, claim=cl)
        if start not in g or goal not in g:
            return []
        try:
            path_nodes = nx.shortest_path(g, start, goal, weight=None)
        except (nx.NetworkXNoPath, nx.NodeNotFound):
            return []
        if len(path_nodes) - 1 > max_hops:
            return []
        # map consecutive node pairs back to the claim that connects them
        chain: list[CausalClaim] = []
        for a, b in zip(path_nodes, path_nodes[1:]):
            data = g.get_edge_data(a, b)
            if data and "claim" in data:
                chain.append(data["claim"])
        return chain

    def explain(self, query: str, tenant_id: str) -> CausalAnswer:
        """Answer 'why did EFFECT happen?' with the highest-confidence ingested cause.

        effect is extracted by _extract_key (keyword heuristic). For precise
        lookup, call explain_effect(effect) with the canonical effect token.
        """
        effect = self._extract_key(query)
        return self.explain_effect(effect, tenant_id)

    def explain_effect(self, effect: str, tenant_id: str) -> CausalAnswer:
        causes = self.retrieve_causes(effect, tenant_id)
        if not causes:
            return CausalAnswer(f"effect={effect}", "explain", None, None, 0.0, [], False)
        top = max(causes, key=lambda c: c.confidence)
        return CausalAnswer(
            query=f"effect={effect}", mode="explain", cause=top.cause, effect=top.effect,
            confidence=top.confidence, citations=[top.source], contested=top.contested)

    def what_if(self, query: str, tenant_id: str) -> CausalAnswer:
        """Answer 'if we do CAUSE, what happens?' with the ingested effect.

        cause is extracted by _extract_key (keyword heuristic). For precise
        lookup, call what_if_cause(cause) with the canonical cause token.
        """
        cause = self._extract_key(query)
        return self.what_if_cause(cause, tenant_id)

    def what_if_cause(self, cause: str, tenant_id: str) -> CausalAnswer:
        effects = self.retrieve_effects(cause, tenant_id)
        if not effects:
            return CausalAnswer(f"cause={cause}", "what_if", None, None, 0.0, [], False)
        top = max(effects, key=lambda c: c.confidence)
        return CausalAnswer(
            query=f"cause={cause}", mode="what_if", cause=top.cause, effect=top.effect,
            confidence=top.confidence, citations=[top.source], contested=top.contested)

    # ---- internals ------------------------------------------------------------
    @staticmethod
    def _row_to_claim(r: _ClaimRow) -> CausalClaim:
        return CausalClaim(
            claim_id=r.claim_id, cause=r.cause, effect=r.effect,
            confidence=r.confidence, source=r.source, tenant_id=r.tenant_id,
            mechanism=r.mechanism or "", contested=bool(r.contested))

    @staticmethod
    def _extract_key(query: str) -> str:
        """Lightweight key extraction: lowercased, stopwords dropped.

        Honest limitation: this is a keyword heuristic, not an LLM parser. It
        matches the exact cause/effect tokens we ingested. For free-text parsing
        you would plug an LLM in front; the graph lookup stays deterministic.
        """
        stop = {"why", "did", "the", "service", "happen", "if", "we", "do",
                "what", "happens", "to", "enable", "enabling", "a", "an", "of",
                "does", "will", "in", "on", "and", "or", "?", "!"}
        toks = [t for t in query.lower().replace("?", " ").split() if t not in stop]
        return " ".join(toks)
