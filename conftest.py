"""Repo-root conftest.

The repository layout places each product's importable package under
``<product>/src/<package>`` (src-layout) while an identically named directory
(``aegis/``, ``causala/``, ``simforge/``) sits at the repository root. When pytest
is invoked from the repository root, Python otherwise treats those root
directories as namespace packages and shadows the *real* editable-installed
packages. This conftest makes the installed ``src`` packages authoritative so
``import aegis`` resolves to ``aegis/src/aegis`` (where ``aegis.spine`` lives),
not the empty root ``aegis/`` directory.
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

# Prepend each product's src/ directory so its package wins over any same-named
# directory at the repo root. Order: src dirs first, then existing path.
src_dirs = [
    os.path.join(ROOT, "aegis", "src"),
    os.path.join(ROOT, "causala", "src"),
    os.path.join(ROOT, "simforge", "src"),
]
for d in reversed(src_dirs):
    if os.path.isdir(d) and d not in sys.path:
        sys.path.insert(0, d)
