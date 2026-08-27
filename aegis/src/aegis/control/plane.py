"""Subsystem 10 + orchestrator: the room where all 10 subsystems live.

`ControlPlane.boot(bus)` instantiates every subsystem, registers it on the bus,
and exposes them by name. `Panes` is the tenth room: a read-only view/aggregator
that surfaces each subsystem's latest posture (trust tier, open drifts, attested
ROI) so an operator can see the whole control plane in one place.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from ..backbone import ControlEvent, EventBus, Subsystem, register_subsystem
from . import (autonomous_ops, causal_decisions, contract_intel, governed_memory,
              roi_attest, sim_rl_factory, swapwatch, twin_truth)
from .swapwatch import SwapWatch
from .roi_attest import ROIAttest
from .governed_memory import GovernedMemory
from .contract_intel import ContractIntel
from .twin_truth import TwinTruth
from .causal_decisions import CausalDecisions
from .sim_rl_factory import SimRLFactory
from .autonomous_ops import AutonomousOps


class Panes:
    name = "panes"

    def __init__(self, state_dir: str):
        self.state_dir = state_dir

    def register(self, bus: EventBus, spine) -> None:
        register_subsystem(self)

    def posture(self, control: "ControlPlane") -> dict:
        out: dict[str, object] = {}
        ops = control.get("autonomous_ops")
        if ops is not None:
            out["trust_tiers"] = dict(ops._tiers)
        sw = control.get("swapwatch")
        if sw is not None:
            drifts = 0
            if Path(sw._ledger).exists():
                for raw in Path(sw._ledger).read_text(encoding="utf-8").splitlines():
                    if "drift" in raw:
                        drifts += 1
            out["open_drifts"] = drifts
        return out


class ControlPlane:
    def __init__(self, spine, state_dir: str):
        self.spine = spine
        self.state_dir = state_dir
        self.subsystems: list[Subsystem] = []
        self._by_name: dict[str, Subsystem] = {}

    def boot(self, bus: EventBus) -> None:
        # The ten rooms of the control plane.
        self.subsystems = [
            SwapWatch(self.state_dir),
            ROIAttest(self.spine),
            GovernedMemory(self.state_dir),
            ContractIntel(self.state_dir),
            TwinTruth(self.state_dir),
            CausalDecisions(self.state_dir),
            SimRLFactory(self.state_dir),
            AutonomousOps(self.state_dir),
            Panes(self.state_dir),
            # ship_gate is the API-layer gate (aegis.gate.ShipGate); register a
            # bus-facing adapter so it appears as a room too.
            _GateRoom(self.spine, self.state_dir),
        ]
        for s in self.subsystems:
            s.register(bus, self.spine)
            self._by_name[s.name] = s

    def get(self, name: str) -> Subsystem | None:
        return self._by_name.get(name)


class _GateRoom:
    """Bus-facing adapter so the Ship Gate is also a first-class room."""

    name = "ship_gate"

    def __init__(self, spine, state_dir: str):
        from ..gate import ShipGate
        self._gate = ShipGate(spine, state_dir=state_dir)

    def register(self, bus: EventBus, spine) -> None:
        register_subsystem(self)

    def evaluate(self, run_id, agent_name, tenant_id, candidate_summary):
        from ..gate import GateRequest
        return self._gate.evaluate(GateRequest(run_id=run_id, agent_name=agent_name,
                                                tenant_id=tenant_id,
                                                candidate_summary=candidate_summary))
