# Providers and references

`Factory[T](factory: Callable[P, T], /, *args: P.args, **__pyinject_kwargs: P.kwargs)`
and `Singleton[T](factory: Callable[P, T], /, *args: P.args, **__pyinject_kwargs: P.kwargs)`
validate all supported bindings at declaration. Constructors are positional-only in
the API, so a target callable may itself accept a keyword named `factory`.

`Provider[T]` is the common graph declaration. Class access preserves Factory or
Singleton; instance access produces `BoundProvider[T]`, whose `__call__() -> T`
accepts no arguments. Unbound declarations are not callable. The descriptor
requires a container at runtime; the static descriptor protocol cannot prove
that its owner is a valid container.

Both declaration and bound provider have read-only `.ref: T`. This is a deliberate
DSL boundary: the future runtime value is a symbolic `Ref[T]`, **not** an instance
of T. Ref has no public construction contract in v0. It must only be used in
provider bindings. The passing `ordinary_service` fixture demonstrates why a
checker cannot guarantee runtime correctness outside the DSL.

| Callable shape | v0 contract |
| --- | --- |
| Plain annotated function | Supported; argument names/types and completeness checked |
| Annotated class constructor | Supported; result is the class instance |
| Positional-only / keyword-only | Supported; preserved by ParamSpec |
| Callable instance / bound method | Supported when it exposes one concrete annotated signature |
| Generic callable | Not guaranteed; specialize via an annotated concrete wrapper |
| Overloaded callable | Not guaranteed; select a concrete annotated wrapper |
| Untyped / Any-based callable | Unsupported; no claim of sound bindings |
| Async / generator factory | Outside v0; no automatic await or resource lifecycle |

Generic and overloaded callables may be accepted by a checker, but v0 does not
promise specialization consistent between both tools. No broad `Any` fallback or
checker plugin is used to hide those limitations. Async *consumers* are distinct
from async *providers*.

## Reserved internal binding name

`__pyinject_kwargs` is reserved by Factory and Singleton. Neither target callable
parameters with that name nor DSL keyword bindings with that spelling are supported.
The future runtime must reject those declarations with InvalidGraphError before
construction. All ordinary names, including `factory`, `self`, `args` and `kwargs`,
remain supported. This restriction was explicitly approved by the user after review.

The reason is a reproduced Pyright 1.1.414/1.1.413 ParamSpec bug: a keyword matching
the forwarding **pack name can be silently ignored, or reported missing even when
supplied. Moving that pack to the reserved name fixes ordinary `kwargs` binding
without changing client syntax. Renaming alone cannot eliminate the upstream bug;
the private spelling is deliberately outside the supported DSL. No checker plugin,
Any, cast or ignored error is involved.

`tests/typing/binding_names/` proves valid/invalid function and constructor bindings,
including required and defaulted `kwargs`. `tests/typing/reserved_bindings/negative.py`
preserves the minimal remaining counterexample: mypy rejects the reserved spelling,
while Pyright emits no diagnostic. The harness records this disagreement explicitly
with `pyright=none`; it does not claim supported behavior for that input.
