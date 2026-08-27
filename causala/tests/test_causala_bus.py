"""CAUSALA integration with the AEGIS control bus."""
from __future__ import annotations

from aegis.backbone import ControlEvent, EventBus, reset_registry

from causa.service import CausalaSubsystem


def test_causala_registers_and_consumes_ingest_event(tmp_path):
    reset_registry()
    bus = EventBus()
    sub = CausalaSubsystem(str(tmp_path / "causala.db"))
    sub.register(bus, None)
    # publish a causal_ingest event on the bus
    bus.publish(ControlEvent("causala", "causal_ingest",
                             {"cause": "flag_on", "effect": "hotspot",
                              "confidence": 0.8, "source": "inc-9"},
                             tenant_id="acme"))
    # now the engine should know the cause
    ans = sub.explain("hotspot", tenant_id="acme")
    assert ans.cause == "flag_on"
    assert "inc-9" in ans.citations
    reset_registry()
