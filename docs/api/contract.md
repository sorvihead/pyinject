# Public API v0 — type design only

U1–U8 deliver declarations, fixtures and contracts. They do **not** deliver a
working dependency injector. The only source of public types is `src/pyinject/*.pyi`;
the runtime package contains no implementations. Type-only examples must not be executed.

Python >=3.15 is the baseline (existing project choice; 3.15.0 is stable since
2026-10-09: https://www.python.org/downloads/release/python-3150/).
Verified toolchain: CPython 3.15.2, mypy 2.4.1, Pyright 1.1.414.
FastAPI 0.162.5 is pinned for U7 source analysis.
`uv.lock` pins the complete development environment; neither checker is a runtime dependency.
No plugins or PEP 827 toolchain are used.

```sh
uv sync --locked
uv run --locked python scripts/check_typing.py
uv run --locked python -m pytest -q
```

The harness invokes mypy strict and Pyright strict separately, with Python 3.15
and `src` as the import root. Positive files and examples must have no diagnostics.
Negative examples use `# E: mypy=CODE pyright=RULE` on the precise failing line.
Comma-separated codes allow multiple diagnostics; `none` denotes an explicitly documented checker limitation for unsupported
inputs (the reserved private binding name). Every diagnostic must match path, line and code, including
multiplicity. Missing, extra, misplaced or unparsable diagnostics fail the gate.

## Public surface

| Module | Public names | Unit |
| --- | --- | --- |
| pyinject | providers, DeclarativeContainer, Provide, Provider, inject | U2/U3/U6 |
| pyinject.providers | Ref, Provider, BoundProvider, Factory, Singleton | U2 |
| pyinject.providers | Dependency, DependenciesContainer | U4 |
| pyinject.providers | FactoryAggregate | U5 |
| pyinject.wiring | Provide, Provider, inject | U6 |
| pyinject.exceptions | PyInjectError and documented diagnostic subclasses | U3/U5/U6 |

`providers.Provider` is a provider declaration type. Root `Provider` is the wiring
marker; the two roles intentionally use separate namespaces.

Runtime requirements are tracked in `runtime-scenarios.md` as future U9–U11 tests.
Passing these static checks or importing the empty package does not prove DI works.
The upstream requirements are preserved in `source-spec.md`.

The frozen export list and complete signatures are in [reference.md](reference.md).
The harness also checks public stubs, its own implementation and its pytest tests.
`reportMissingModuleSource` is disabled only because this phase intentionally
ships type-only modules. Missing imports and unknown types remain errors.
Negative statements use `fmt: off` where wrapping would move diagnostics away
from their expected line; this suppresses formatting only, never type errors.
