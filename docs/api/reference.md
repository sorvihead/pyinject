# Public API v0 reference

**API gate:** U1–U8 describe and statically verify the API. No resolver, bound
execution, cache or injection is implemented. The package has no runtime
dependencies; FastAPI and checkers are development dependencies only. Do not run
these examples as working DI applications. U9–U11 will replace the type-only
modules without changing these signatures.

## Exports

| Module | Exports |
| --- | --- |
| `pyinject` | `providers`, `DeclarativeContainer`, `Provide`, `Provider`, `inject` |
| `pyinject.containers` | `DeclarativeContainer` |
| `pyinject.providers` | `Ref[T]`, `Provider[T]`, `BoundProvider[T]`, `Factory[T]`, `Singleton[T]`, `Dependency[T]`, `DependenciesContainer[C]`, `FactoryAggregate[T]`, `BoundFactoryAggregate[T]` |
| `pyinject.wiring` | `Provide`, `Provider`, `inject` |
| `pyinject.exceptions` | all classes in the errors table below |

Root `Provider` is the wiring marker. `providers.Provider[T]` is the graph
provider base. Marker implementation types, execution contexts and resolvers are
private. Ref is a symbolic type, not a user-constructed value in this version.

## Signatures

All listed properties are read-only. Constructor and method `/` and `*` separators
are significant. P is a ParamSpec, T is the result, C extends DeclarativeContainer.

```text
Factory[T](factory: Callable[P, T], /, *args: P.args, **__pyinject_kwargs: P.kwargs)
Singleton[T](factory: Callable[P, T], /, *args: P.args, **__pyinject_kwargs: P.kwargs)
Dependency[T](source: providers.Provider[T], /)
DependenciesContainer[C](container: type[C], /)
FactoryAggregate[T](**factories: Factory[T])

Provider[T].ref -> T
Provider[T].__get__(None, owner) -> Provider[T]
Provider[T].__get__(instance, owner) -> BoundProvider[T]
Factory/Singleton/Dependency class access preserves its concrete declaration type
BoundProvider[T]() -> T
BoundProvider[T].ref -> T

DependenciesContainer[C].providers -> type[C]   # inside declaration
DependenciesContainer[C].__get__(None, owner) -> type[C]
DependenciesContainer[C].__get__(instance, owner) -> C

FactoryAggregate[T].ref -> Callable[[str], T]
FactoryAggregate[T].__get__(None, owner) -> FactoryAggregate[T]
FactoryAggregate[T].__get__(instance, owner) -> BoundFactoryAggregate[T]
BoundFactoryAggregate[T](key: str) -> T
BoundFactoryAggregate[T].ref -> Callable[[str], T]

DeclarativeContainer()
DeclarativeContainer.wire(*, modules: Sequence[ModuleType]) -> None
DeclarativeContainer.unwire() -> None
inject(function: Callable[P, R], /) -> Callable[P, R]
Provide[providers.Provider[T]] -> T
Provider[providers.Provider[T]] -> private callable () -> T
Provide[FactoryAggregate[T]] -> Callable[[str], T]
Provider[FactoryAggregate[T]] -> private callable () -> Callable[[str], T]
```

## Errors (future runtime)

All inherit `PyInjectError(Exception)`. Messages carry qualified source paths;
constructor failures additionally preserve their cause. No extra public error
attributes or custom constructors are part of v0.

| Exception | Trigger and time |
| --- | --- |
| `InvalidContainerError` | concrete-container inheritance, at class creation |
| `InvalidGraphError` | unsupported/mutated declaration, reserved binding name or empty aggregate, at graph validation/binding |
| `UnboundProviderError` | resolving a declaration without context, before construction |
| `CircularDependencyError` | cycle during resolution; ordered path with repeated node |
| `ResolutionError` | application constructor failure during resolution; `__cause__` retained; retry allowed |
| `UnknownFactoryError` | missing selector key at aggregate call, before a constructor; list available keys |
| `UnreachableProviderError` | root cannot reach marker source, at wire; registration is atomic |
| `WiringConflictError` | function already bound to another root, at wire; old binding retained |
| `UnwiredError` | marker needs resolution without a root, before user body |

Ordinary Python call-binding/type errors remain TypeError. Static checks do not
prove runtime exception behavior. Runtime tests are planned in
[runtime-scenarios.md](runtime-scenarios.md).

## Contracts and complete checked examples

- [Providers](providers.md): full bindings and callable support matrix;
  `tests/typing/providers/` proves both valid and invalid declarations.
- [Containers](containers.md): blueprint, binding, source identity, isolation,
  cycle and inheritance contract; `tests/typing/containers/` proves static types.
- [Composition](composition.md): result-preserving Dependency and named group
  projection; [application example](../../examples/application.py).
- [Aggregate](aggregate.md): common result T, Factory-only children and callable
  ref; [application example](../../examples/application.py) includes a consumer.
- [Wiring](wiring.md): default markers, explicit arguments and idempotent module
  registration; [sync/async example](../../examples/functions.py).
- [FastAPI analysis](fastapi.md): standard Depends, decorator order, inspected
  marker protocol and caching limits; [FastAPI example](../../examples/fastapi_app.py).
- [Verification matrix](contract.md) and [requirement traceability](traceability.md).

## Explicit limits

`.ref` and Provide defaults are typed as T but are symbolic at runtime. Group
projections are typed as C/type[C] only to expose provider members; they are not
independent source containers. Annotated metadata does not validate a Depends
result against the annotated type. Positive fixtures deliberately demonstrate
these static blind spots. Public usage examples contain no Any, cast or ignored
type errors. Unsupported generic/overload callables use concrete wrappers.

`__pyinject_kwargs` is reserved for provider internals; target parameters and DSL
bindings with that spelling are unsupported. See [the reproduced checker
limitation and approved restriction](providers.md#reserved-internal-binding-name).
The future runtime rejects such declarations with InvalidGraphError.

No partial initialization, overrides, Resource, Configuration, automatic
registration, async providers, request scopes or checker plugins are included.
Concurrency enforcement must be designed in U9 before Singleton runtime ships.
PEP 827 remains an independent U12 experiment, with no dependency in this stack.
