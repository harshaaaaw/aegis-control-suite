"""SIMFORGE observability: OpenTelemetry counters (mirror of AEGIS/CAUSALA)."""
from __future__ import annotations

from opentelemetry import metrics

_meter = metrics.get_meter("simforge", "0.1.0")

SIMS = _meter.create_counter("simforge.sims", description="Simulations run, by tenant")
FORGES = _meter.create_counter("simforge.forges", description="Golden cases forged, by tenant")


def record_sim(tenant: str) -> None:
    SIMS.add(1, {"tenant": tenant})


def record_forge(tenant: str) -> None:
    FORGES.add(1, {"tenant": tenant})
