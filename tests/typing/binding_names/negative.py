# fmt: off
from tests.typing.binding_names.positive import NamedConstructor, optional, ordinary, required

from pyinject import providers

providers.Factory(ordinary, 1, kwargs=123)  # E: mypy=call-arg pyright=reportCallIssue
providers.Singleton(ordinary, 1, kwargs=123)  # E: mypy=call-arg pyright=reportCallIssue
providers.Factory(optional, kwargs=123)  # E: mypy=arg-type pyright=reportArgumentType
providers.Singleton(optional, kwargs=123)  # E: mypy=arg-type pyright=reportArgumentType
providers.Factory(NamedConstructor, kwargs=123)  # E: mypy=arg-type pyright=reportArgumentType
providers.Singleton(NamedConstructor, kwargs=123)  # E: mypy=arg-type pyright=reportArgumentType
providers.Factory(required)  # E: mypy=call-arg pyright=reportCallIssue
providers.Singleton(required)  # E: mypy=call-arg pyright=reportCallIssue
# fmt: on
