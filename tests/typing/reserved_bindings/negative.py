# fmt: off
from tests.typing.binding_names.positive import ordinary

from pyinject import providers

# Unsupported DSL spelling: the private binding-pack identifier is reserved.
# mypy still detects misuse; Pyright has the documented upstream blind spot.
providers.Factory(ordinary, 1, __pyinject_kwargs=123)  # E: mypy=call-arg pyright=none
providers.Singleton(ordinary, 1, __pyinject_kwargs=123)  # E: mypy=call-arg pyright=none
# fmt: on
