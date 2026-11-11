from collections.abc import Callable
from typing import assert_type, final

from tests.typing.models import OtherService, Repository, Service

from pyinject import DeclarativeContainer, providers


class Consumer:
    def __init__(self, choose: Callable[[str], Service]) -> None:
        self.choose = choose


@final
class Application(DeclarativeContainer):
    repository = providers.Singleton(Repository, "memory:")
    service = providers.FactoryAggregate[Service](
        primary=providers.Factory(Service, repository.ref),
        alternate=providers.Factory(OtherService, repository.ref),
    )
    consumer = providers.Factory(Consumer, choose=service.ref)


app = Application()
assert_type(app.service("primary"), Service)
assert_type(app.service("alternate"), Service)
assert_type(app.service.ref, Callable[[str], Service])
assert_type(Application.service.ref, Callable[[str], Service])
assert_type(app.consumer(), Consumer)
# Unknown string keys cannot be rejected statically with the common-T API.
assert_type(app.service("unknown"), Service)
