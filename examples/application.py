"""Type-only API example. DI runtime is deferred to U9-U11."""

from collections.abc import Callable
from typing import final

from examples.domain import OtherService, Repository, Service

from pyinject import DeclarativeContainer, providers


class Consumer:
    def __init__(self, choose: Callable[[str], Service]) -> None:
        self.choose = choose


@final
class Infrastructure(DeclarativeContainer):
    repository = providers.Singleton(Repository, dsn="memory:")


@final
class Application(DeclarativeContainer):
    repository = providers.Dependency(Infrastructure.repository)
    infrastructure = providers.DependenciesContainer(Infrastructure)
    service = providers.Factory(Service, repo=repository.ref)
    grouped_service = providers.Factory(Service, repo=infrastructure.providers.repository.ref)
    services = providers.FactoryAggregate[Service](
        primary=providers.Factory(Service, repo=repository.ref),
        alternate=providers.Factory(OtherService, repo=repository.ref),
    )
    consumer = providers.Factory(Consumer, choose=services.ref)
