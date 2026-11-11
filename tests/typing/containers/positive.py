from typing import assert_type, final

from tests.typing.models import Repository, Service

from pyinject import DeclarativeContainer, providers


@final
class Application(DeclarativeContainer):
    repository = providers.Singleton(Repository, "memory:")
    service = providers.Factory(Service, repository.ref)


@final
class AnotherApplication(DeclarativeContainer):
    service = providers.Factory(Service, Repository("memory:"))


app = Application()
assert_type(Application.service, providers.Factory[Service])
assert_type(app.service, providers.BoundProvider[Service])
assert_type(app.service(), Service)
assert_type(app.repository(), Repository)
