# Requirements and verification evidence

The exact requirements are preserved in [source-spec.md](source-spec.md).
`python scripts/check_typing.py` runs all listed fixtures with mypy 2.4.1 and
Pyright 1.1.414. Future runtime scenarios below are specifications, not passing tests.

| Requirement | Static artifact / checked example | Future runtime evidence |
| --- | --- | --- |
| R1 declarations | providers/, containers/; examples/application.py | U9 bound resolution |
| R2 complete bindings | providers/negative.py; containers/negative.py; aggregate/negative.py | U9 no late bindings |
| R3 .ref | providers/positive.py; composition/positive.py | U9 symbolic Ref resolution |
| R4 argument checking | providers/ positive/negative; binding_names/ proves ordinary names including kwargs; reserved_bindings/ captures the approved private-name limit | U9 binding diagnostics |
| R5 blueprint | containers.md; containers/positive.py | U9 constructors not called on declaration/Container() |
| R6 scopes | containers.md; runtime-scenarios.md | U9 freshness, identity, isolation, retry, concurrency |
| R7 no concrete inheritance | containers/negative.py and explicit @final examples | U9 independent runtime enforcement |
| R8 configured proxy | composition/ positive/negative; examples/application.py | U10 shared source identity/root context |
| R9 typed group | composition/ positive/negative; .providers and class/instance projections | U10 no hidden source container |
| R10 aggregate | aggregate/ positive/negative; callable consumer example | U10 keys, no cache, context propagation |
| R11 ordinary functions | wiring/ positive/negative; examples/functions.py | U11 default resolution, explicit arguments, coroutine identity |
| R12 FastAPI | fastapi/ positive/negative; examples/fastapi_app.py | U11 sync/async HTTP, required direct calls, schema |
| R13 standard Depends/module wiring | wiring.md, fastapi.md pinned-source analysis | U11 module reachability, idempotence, conflict, unwire |
| R14 boundaries | providers/positive.py (outside DSL), fastapi/positive.py (metadata mismatch), composition.md | No claim of soundness; U9/U11 must reject unresolved markers |
| R15 API before runtime | .pyi-only API, reference.md; empty runtime package | U9–U11 only after gate |
| R16 separate experiment | dependency groups/uv.lock contain no PEP 827 tools | U12 separate branch, not executed here |

KTD1: ParamSpec and generic-instance getitem fixtures. KTD2: source identity/root
context contract. KTD3: explicit @final versus runtime inheritance enforcement.
KTD4: Dependency[T] and concrete group projection proof. KTD5: separate aggregate
selector. KTD6: atomic, repeatable module wiring contract. KTD7: sync providers,
async consumers and pinned FastAPI source analysis. KTD8: strict, locked checker
matrix, path/line/code-exact negative diagnostics and CI.

The API-shape gates (U4 composition, U5 aggregate, U6 markers, U7 FastAPI source
compatibility) have concrete type proofs and documented runtime boundaries.
There is no unresolved API-shape blocker; DI execution remains intentionally
unimplemented. A successful static gate permits starting U9, not claiming a
working injector.
