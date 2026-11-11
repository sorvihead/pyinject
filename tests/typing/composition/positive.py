from typing import assert_type, final

from tests.typing.models import Repository, Service

from pyinject import DeclarativeContainer, providers


@final
class Infrastructure(DeclarativeContainer):
    repository = providers.Singleton(Repository, dsn="memory:")


@final
class Application(DeclarativeContainer):
    repository = providers.Dependency(Infrastructure.repository)
    another_repository = providers.Dependency(Infrastructure.repository)
    service = providers.Factory(Service, repo=repository.ref)
    infrastructure = providers.DependenciesContainer(Infrastructure)
    grouped_service = providers.Factory(Service, repo=infrastructure.providers.repository.ref)


app = Application()
assert_type(Application.repository, providers.Dependency[Repository])
assert_type(Application.repository.ref, Repository)
assert_type(Application.infrastructure, type[Infrastructure])
assert_type(Application.infrastructure.repository, providers.Singleton[Repository])
assert_type(app.infrastructure, Infrastructure)
assert_type(app.infrastructure.repository(), Repository)
assert_type(app.repository(), Repository)
assert_type(app.service(), Service)
assert_type(app.grouped_service(), Service)
