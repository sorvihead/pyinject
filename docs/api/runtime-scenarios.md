# Future runtime verification (not executed by the API phase)

These are requirements for U9–U11, not passing tests or implemented guarantees.

## U9

- Declaration and Container() never construct application objects.
- Factory creates fresh values; Singleton reuses a value within a root context,
  and isolates two root instances. Choose and test a concurrency contract before implementation.
- Only direct DeclarativeContainer subclasses are allowed at runtime; @final is
  an explicit static aid, not runtime enforcement.
- Class-level resolution has no context and fails. Cycles show a qualified node path.
- Constructor failures retain their cause and permit a later retry without poisoning the cache.

## U10

- Dependency proxies share the source node's identity and root execution context.
- Group projection does not instantiate a hidden source container.
- Aggregate factories share nested singleton dependencies; unknown keys fail explicitly.

## U11

- Resolve markers only when needed, before entering the user body.
- Explicit arguments take precedence; missing wiring with explicit arguments works.
- wire/unwire repetition and cross-context conflicts follow the documented contract.
- Real FastAPI sync/async requests receive objects, not markers; OpenAPI has no
  accidental args/kwargs. Measure dependency caching and use_cache=False separately.
