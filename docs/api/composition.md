# Typed composition

`Dependency[T](source: Provider[T], /)` is a fully configured proxy, not an empty
slot. The mandatory `Dependency(Infrastructure.repository)` example infers
`Dependency[Repository]` and `.ref: Repository` on both checkers. Source node
identity and root context are preserved; two proxies of one source Singleton
share its value inside one Application, and two Applications remain isolated.
There is no hidden Infrastructure() or dependency constructor argument.

The public proxy preserves **result T**, not concrete provider P. Preserving
`P: Provider[...]` alone does not project an associated result type in Python's
standard type system. Encoding P *and* T would add a redundant public parameter.
The executable proof tests inferred `Dependency[Repository]`, its reference and
its bound call; errors show incompatible Repository/Service wiring is rejected.

## Groups

`DependenciesContainer[C: DeclarativeContainer](container: type[C], /)` is a
read-only descriptor/projection with three precise access forms:

| Access | Static type | Future runtime meaning |
| --- | --- | --- |
| `group.providers` inside the class body | `type[C]` | symbolic projection of source declarations |
| `Application.group` | `type[C]` | same declaration projection |
| `Application().group` | `C` | projection bound to this root context |

```python
@final
class Application(DeclarativeContainer):
    infrastructure = providers.DependenciesContainer(Infrastructure)
    service = providers.Factory(Service, repo=infrastructure.providers.repository.ref)


app = Application()
repo = app.infrastructure.repository()
```

The complete, checked version is `tests/typing/composition/positive.py`.
Unknown members and non-container inputs are rejected. No permissive __getattr__
or public Any is used. This design retains named members by projecting the
concrete container type, rather than pretending a wrapper can forward arbitrary
attributes statically.

`type[C]`/`C` represent a **projection**, not a genuine independent source class
or constructed source container. The projection supports provider access only;
calling the class projection or using source-container lifecycle methods through
it is unsupported even if accepted statically. Use the root for wire/unwire.
This is an explicit static/runtime boundary like `.ref`, not a promise that
projections are general-purpose C instances. Read-only graph enforcement and
context propagation belong to U10.
