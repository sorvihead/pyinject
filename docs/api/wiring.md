# Module wiring

Root and `pyinject.wiring` export `Provide`, `Provider` and `inject`.
`Provide` and `Provider` are singleton marker-factory **instances**, with generic
instance `__getitem__`, not generic classes. Their implementation types are private.
`providers.Provider[T]` is the separate declaration class.

| Input | `Provide[...]` | `Provider[...]()` |
| --- | --- | --- |
| `providers.Provider[T]` declaration | T | T |
| `FactoryAggregate[T]` declaration | Callable[[str], T] | Callable[[str], T] |

These types deliberately describe eventual injected results. Actual default
markers and callable return tokens are symbolic until injection. Outside wired
DSL consumption they are not real values; static acceptance is not soundness.
Only declarations are accepted, not arbitrary objects or already bound providers.

`inject(function: Callable[P, R], /) -> Callable[P, R]` preserves parameter names,
required parameters, defaults, keyword-only parameters, result and coroutine
shape. A default `service: Service = Provide[Application.service]` may be omitted;
a caller may pass an explicit Service, which always wins. Business arguments
remain required. Both sync and async consumer functions are supported with
synchronous providers. No async provider support follows from this.

## Future runtime behavior (U11)

`app.wire(*, modules: Sequence[ModuleType]) -> None` discovers `@inject` functions
in the supplied module objects (module strings and recursive package scanning are
not v0 API). No global auto-wiring or separate setup(app) call is required.
`app.unwire() -> None` removes this root's registrations.

Each decorated function has at most one active root execution context. That root
must reach **every** provider declaration in the function's markers through its
blueprint, including original source nodes behind Dependency/group projections.
`wire` validates reachability before modifying any registrations and raises
`UnreachableProviderError` with function, parameter and provider paths if invalid.
It does not resolve providers or run constructors. Modules must be imported and
functions decorated before wiring.

Rewiring to the same context is idempotent; repeated calls may add modules.
Binding an already wired function to another live context raises
`WiringConflictError` atomically, preserving the old registrations. Calling
unwire repeatedly is harmless; it removes only bindings owned by that instance.
After unwire, another root may wire the same functions.

At each function call, bind Python arguments first, keep explicit values, and
resolve only remaining marker defaults. Missing wiring raises `UnwiredError`
**before the user body**, but only if a marker needs resolution. A completely
explicit call works without wiring, including after unwire. Constructor and cycle
errors propagate according to the provider contract. A marker supplied by FastAPI
is resolved before the endpoint body; its callable protocol is specified in
`fastapi.md`. Ordinary explicitly supplied concrete objects are never overwritten.

The wrapper must preserve `__wrapped__`, inspected signature, annotations and
coroutine-function identity; the type-preserving decorator declaration alone
does not prove these runtime properties. Method injection, decorator stacks that
destroy signatures and dynamic module mutation after wire are outside v0.
