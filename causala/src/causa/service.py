"""CAUSALA as an AEGIS control-plane subsystem.

Reuses the AEGIS backbone (event bus + failure isolation) so CAUSALA slots into
the same 'room' as the other 10 subsystems. It consumes causal-ingest / causal-
query events and persists to its own externalized causal store. This is the
Information-Retrieval layer of the control plane: agents ask CAUSALA 'why?' and
get citation-backed causal answers instead of vibes.
"""
from __future__ import annotations

from aegis.backbone import ControlEvent, EventBus, Subsystem, register_subsystem
from aegis.security import get_logger

from . import Causala, CausalAnswer

log = get_logger("causala.service")


class CausalaSubsystem:
    name = "causala"

    def __init__(self, db_path: str):
        self._db_path = db_path
        self._engine = Causala(db_path)

    def register(self, bus: EventBus, spine) -> None:
        bus.subscribe(self.name, self.handle)
        register_subsystem(self)

    def handle(self, event: ControlEvent) -> None:
        if event.kind == "causal_ingest":
            p = event.payload
            self._engine.ingest_claim(
                cause=p["cause"], effect=p["effect"], confidence=p["confidence"],
                source=p["source"], tenant_id=event.tenant_id or "acme",
                mechanism=p.get("mechanism", ""))
            log.info("causal_ingest", extra={"tenant": event.tenant_id, "cause": p["cause"]})
        elif event.kind == "causal_explain":
            p = event.payload
            ans = self._engine.explain_effect(p["effect"], tenant_id=event.tenant_id or "acme")
            log.info("causal_explain", extra={"effect": p["effect"], "cause": ans.cause})

    # convenience delegates so the API/CLI can call the engine directly
    def explain(self, effect: str, tenant_id: str) -> CausalAnswer:
        return self._engine.explain_effect(effect, tenant_id)

    def what_if(self, cause: str, tenant_id: str) -> CausalAnswer:
        return self._engine.what_if_cause(cause, tenant_id)

    def ingest(self, cause: str, effect: str, confidence: float,
               source: str, tenant_id: str, mechanism: str = "") -> str:
        return self._engine.ingest_claim(cause, effect, confidence, source,
                                         tenant_id, mechanism)

    def path(self, start: str, goal: str, tenant_id: str, max_hops: int = 4):
        return self._engine.retrieve_path(start, goal, tenant_id, max_hops)
