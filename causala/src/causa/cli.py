"""Consumer-friendly CAUSALA CLI (zero config, reuses AEGIS bus patterns).

    causala ingest  --cause cache_miss --effect cost_up --conf 0.8 --source finops-3
    causala explain --effect cost_up
    causala whatif  --cause cache_miss
    causala path    --from cache_miss --to db_hotspot
"""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

import typer

from . import Causala
from .service import CausalaSubsystem

app = typer.Typer(help="CAUSALA: causal-inference retrieval over a compiled causal layer.")
_DB = str(Path(tempfile.gettempdir()) / "causala.db")


def _engine() -> Causala:
    return Causala(_DB)


@app.command()
def ingest(cause: str = typer.Option(..., "--cause"),
          effect: str = typer.Option(..., "--effect"),
          conf: float = typer.Option(..., "--conf"),
          source: str = typer.Option(..., "--source"),
          tenant: str = "local", mechanism: str = ""):
    cid = _engine().ingest_claim(cause, effect, conf, source, tenant, mechanism)
    typer.echo(json.dumps({"claim_id": cid, "cause": cause, "effect": effect,
                           "confidence": conf, "source": source}, indent=2))


@app.command("explain")
def explain(effect: str = typer.Option(..., "--effect"), tenant: str = "local"):
    ans = _engine().explain_effect(effect, tenant)
    typer.echo(json.dumps({"cause": ans.cause, "effect": ans.effect,
                           "confidence": ans.confidence, "citations": ans.citations,
                           "contested": ans.contested}, indent=2))


@app.command("whatif")
def whatif(cause: str = typer.Option(..., "--cause"), tenant: str = "local"):
    ans = _engine().what_if_cause(cause, tenant)
    typer.echo(json.dumps({"cause": ans.cause, "effect": ans.effect,
                           "confidence": ans.confidence, "citations": ans.citations}, indent=2))


@app.command("path")
def path(from_: str = typer.Option(..., "--from"), to: str = typer.Option(..., "--to"),
         tenant: str = "local", max_hops: int = 4):
    chain = _engine().retrieve_path(from_, to, tenant, max_hops)
    typer.echo(json.dumps(
        [{"cause": c.cause, "effect": c.effect, "confidence": c.confidence,
          "source": c.source} for c in chain], indent=2))


if __name__ == "__main__":
    app()
