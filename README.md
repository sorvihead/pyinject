# pyinject

A Python dependency injection library, currently in early development.

## Development

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then create
the environment with the versions recorded in `uv.lock`:

```sh
uv sync --locked
```

The project currently requires Python 3.15 or newer. Development tools are in the
`dev` dependency group and are installed by default; the library has no runtime
dependencies.

Run the checks from the repository root:

```sh
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked ty check
```

Apply safe lint fixes, then format the code:

```sh
uv run --locked ruff check --fix .
uv run --locked ruff format .
```

For continuous type checking while developing:

```sh
uv run --locked ty check --watch
```

### Code conventions

- Ruff formats code with an 88-character line length, sorts imports, checks for
  common bugs, and requires function annotations. Tests are exempt from the
  annotation rules. `Any` is allowed for dynamic dependency injection internals.
- ty checks Python files throughout the project, including future tests and
  examples. Warnings fail the check; redundant casts and unused suppression
  comments are errors. The `src` directory is the import root, and type checking
  does not assume a specific operating system.
- Both tools infer the minimum supported Python version from `requires-python`
  in `pyproject.toml`.
- Runtime annotations matter for dependency injection. The configuration does
  not enable rules that require moving imports under `TYPE_CHECKING` or adding
  postponed annotations.
- The package includes `py.typed` so consumers can use its inline type hints.

All settings live in `pyproject.toml`. See the official
[Ruff configuration](https://docs.astral.sh/ruff/configuration/) and
[ty configuration](https://docs.astral.sh/ty/reference/configuration/) references.
