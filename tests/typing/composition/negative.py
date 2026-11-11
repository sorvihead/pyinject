# fmt: off
from tests.typing.composition.positive import Application, Infrastructure
from tests.typing.models import Repository, Service

from pyinject import providers

providers.Dependency(Repository("memory:"))  # E: mypy=arg-type pyright=reportArgumentType
wrong: providers.Dependency[Service] = providers.Dependency( Infrastructure.repository )  # E: mypy=arg-type pyright=reportAssignmentType
providers.Factory(Service, repo=Application.service.ref)  # E: mypy=arg-type pyright=reportArgumentType
_ = ( Application.infrastructure.missing )  # E: mypy=attr-defined pyright=reportAttributeAccessIssue,reportUnknownMemberType,reportUnknownVariableType
_ = ( Application().infrastructure.missing )  # E: mypy=attr-defined pyright=reportAttributeAccessIssue,reportUnknownMemberType,reportUnknownVariableType
providers.DependenciesContainer(Repository)  # E: mypy=type-var pyright=reportArgumentType
# fmt: on
