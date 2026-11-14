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
