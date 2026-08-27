"""FAULT-INJECTION (mutation) tests: prove the suites guard core invariants."""
from __future__ import annotations

import json

from aegis.gate import GateRequest, ShipGate
from aegis.spine import Spine, SpineConfig

from causa import Causala


def _aegis_gate(tmp_path):
    spine = Spine(SpineConfig(db_path=str(tmp_path / "s.db"), jwt_secret="0" * 32))
    state = tmp_path / "g"
    (state / "runs").mkdir(parents=True, exist_ok=True)
    # write a recorded run artifact so evaluate() can certify it
    (state / "runs" / "r.jsonl").write_text(
        json.dumps({"idx": 0, "kind": "MODEL_CALL", "name": "p",
                    "in": {"x": 1}, "out": {"y": 2}, "state": {"x": 1}, "ms": 5}) + "\n")
    return ShipGate(spine, state_dir=str(state))


def test_aegis_tenant_isolation_invariant(tmp_path):
    gate = _aegis_gate(tmp_path)
    vid = gate.evaluate(GateRequest(run_id="r", agent_name="a", tenant_id="acme",
                                    candidate_summary="s")).verdict_id
    assert gate.verify_verdict(vid, tenant_id="acme")[0] is True
    assert gate.verify_verdict(vid, tenant_id="rival")[0] is False  # real check


def test_causala_idempotency_invariant(tmp_path):
    c = Causala(str(tmp_path / "c.db"))
    k = {"cause": "x", "effect": "y", "confidence": 0.8, "source": "s1", "tenant_id": "acme"}
    assert c.ingest_claim(**k) == c.ingest_claim(**k)


def test_causala_tenant_isolation_invariant(tmp_path):
    c = Causala(str(tmp_path / "c.db"))
    c.ingest_claim("a", "b", 0.8, "s1", "acme")
    assert c.explain_effect("b", "rival").cause is None
