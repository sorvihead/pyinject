# Container and execution context contract

`DeclarativeContainer()` has no constructor injection. Only direct subclasses
are valid. Concrete containers use explicit `@final` for static rejection of a
further subclass. Runtime enforcement must independently reject inheritance
from any concrete container, even without `@final`, with `InvalidContainerError`.
Two unrelated direct subclasses are valid.

Class attributes are an immutable blueprint. No application constructors run
while declaring the class or creating a container instance. Mutation, replacing
nodes, partial configuration and overrides are unsupported; v0 exposes no mutation
API. Standard Python typing does not prevent every attribute reassignment.

Access on the class preserves the declaration type (Factory, Singleton or later
Dependency); access through an instance yields a `BoundProvider[T]`. Only its
zero-argument call resolves T. An unbound declaration call is rejected statically
and, for unchecked callers, must raise `UnboundProviderError` before any constructor.

An instance owns one execution context. Singleton cache keys are the pair of
root context and **original source node identity**, never the attribute name or
proxy identity. Factory always creates a new result; Singleton memoizes only a
successful result. Different container instances are isolated. No context or
cache lives on class attributes. Failed construction is wrapped in `ResolutionError`
with the original exception as `__cause__`, a qualified dependency path, and no
cached failed value; a retry is permitted.

Cycles are detected during resolution, before recursing indefinitely, and raise
`CircularDependencyError` with the ordered qualified path including the repeated
node (for example `Application.service -> Infrastructure.repo -> Application.service`).
Invalid graph declarations raise `InvalidGraphError` when binding or validating
the graph, without constructing dependencies. Concurrency and locking are to be
specified in U9; the API phase does not establish thread safety.

All behaviors here are **future runtime contracts**. The .pyi files and static
fixtures prove only the declared types; the scenario inventory is in
`runtime-scenarios.md`.
