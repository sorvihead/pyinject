# FactoryAggregate

`FactoryAggregate[T](**factories: Factory[T])` accepts named, fully configured
Factory children only. Specify the common base explicitly (for example
`FactoryAggregate[Service]`) for heterogeneous implementations; no key-specific
return inference is promised. Singleton, Dependency and nested aggregates are
not valid children. Factory subclasses are allowed if they honor the Factory
contract. Empty aggregate declarations raise `InvalidGraphError` at runtime.

Class access yields a declaration; instance access yields
`BoundFactoryAggregate[T]` with `__call__(key: str) -> T`. No other arguments are
accepted: selection cannot reconfigure the chosen Factory. Keys are case-sensitive
strings; they need not be identifiers when passed with a typed dictionary via **.
No dynamic key-named attributes or Literal key validation are provided.

`.ref: Callable[[str], T]` is a symbolic selector at declaration and a bound
selector in the root execution context. It is **not T** and **not a zero-argument
Provider[T]**. It can be passed to a consumer expecting a callable. The aggregate
has no singleton cache; selected factories retain normal freshness and nested
Singleton dependencies share the same root context.

An unknown key raises `UnknownFactoryError` with the requested key and available
keys before any selected constructor runs. Resolving an unbound declaration
raises `UnboundProviderError`. Validation and selection are future U10 behavior;
the typing fixtures prove only the callable shape and accepted/rejected bindings.
Wiring may inject the selector callable through `Provide[Application.service]`
or `Provider[Application.service]`; it never selects a default key implicitly.
