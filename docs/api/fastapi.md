# Standard FastAPI integration contract

**Evidence:** installed FastAPI **0.162.5**, pinned in the dev group and uv.lock;
source inspection on Python 3.15.2. This is design evidence, **not** an HTTP smoke
or proof of implemented injection. Runtime confirmation belongs to U11.

## Client form and order

```python
@router.get("/items")
@inject
def endpoint(
    service: Annotated[Service, Depends(Provider[Application.service])],
) -> str:
    return service.repo.dsn
```

Python applies inject first, then router registration. Wire the imported endpoint
module using `app.wire(modules=[module])`. Use FastAPI's standard Depends; there
is no custom Depends, setup(app), or client integration adapter. Endpoint service
is required for a direct Python call. The checked sync/async examples are in
`tests/typing/fastapi/positive.py`.

## Source observations

Pinned source links refer to the files actually examined:

- [dependencies/utils.py](https://github.com/fastapi/fastapi/blob/0.162.5/fastapi/dependencies/utils.py):
  `_get_signature` (227), `get_typed_signature` (242), `get_dependant` (300) inspect
  the callable and recurse into Depends callables. `get_typed_signature` unwraps
  for annotation globals. Dependency return annotations do not establish the
  endpoint parameter type. `solve_dependencies` (643; cache branch 717–737)
  supplies dependency results by parameter name; sync callables use a thread pool.
- [dependencies/models.py](https://github.com/fastapi/fastapi/blob/0.162.5/fastapi/dependencies/models.py):
  `_get_cache_key` uses callable plus scopes; `_is_coroutine_callable_cached` (198)
  considers routines, unwrapped routines and callable-instance __call__.
- [routing.py](https://github.com/fastapi/fastapi/blob/0.162.5/fastapi/routing.py):
  `_build_dependant_with_parameterless_dependencies` (907) analyzes the registered
  endpoint immediately. Consequently inject must wrap before router registration;
  registering the undecorated function would bypass injection on HTTP calls.
- [Callable instance dependencies](https://fastapi.tiangolo.com/advanced/advanced-dependencies/):
  confirms a callable instance is an ordinary Depends input.

## Required internal protocol for U11

`Provider[declaration]` must produce a hashable, synchronous callable instance
with an inspected **empty** parameter list. No public args/kwargs and no source
container constructor signature may leak into OpenAPI. Its call returns a private
symbolic token identifying the source node, not a resolved dependency. The marker
must not own a root execution context; the endpoint wrapper owns that binding.

`inject` must preserve __wrapped__, evaluated Annotated metadata and the original
inspected signature. The sync wrapper remains sync; the async wrapper is itself
async. wire must discover both default Provide markers and callable Provider
markers nested in Annotated Depends metadata. The wrapper resolves returned
Provider tokens in its bound root context before the endpoint body. Explicit
concrete Python arguments remain untouched. Unwired token resolution raises
UnwiredError before the body, using the same rules as ordinary function wiring.

This sequence is **inferred compatible** from the pinned source; no observed
source-level blocker remains. Signature preservation, token handling and wrapper
classification must still be proved by integration tests when implemented.

## Caching and boundaries

FastAPI caches the dependency callable's **return token**, not necessarily the
provider result. Equal/hash-identical marker instances for the same source node
may share FastAPI's cache key; U11 must define and test their equality semantics.
`use_cache=False` bypasses the dependency read cache, and FastAPI may still insert
a result for another dependency to reuse. Each injected parameter resolves its
token according to Factory/Singleton rules in the root context. Exact constructor
counts with repeated Depends must be measured in U11, not guessed from the static
signature. No request scope or Factory memoization is promised.

Both checkers accept a mismatched `Annotated[Repository,
Depends(Provider[Application.service])]`. Metadata is not checked against the
annotation. A separate assertion proves the marker call's static return is Service;
it cannot make Annotated sound. The passing mismatch fixture intentionally records
this limitation; it is not a valid runtime example.

U11 must exercise real HTTP sync/async handlers, explicit calls, wire/unwire,
pre-body errors, correct object identity/freshness, query schema without incidental
args/kwargs, repeated dependencies, use_cache=False and concurrent sync handlers.
