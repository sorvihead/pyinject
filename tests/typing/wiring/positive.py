import sys
from collections.abc import Callable
from typing import assert_type

from tests.typing.aggregate.positive import Application as AggregateApplication
from tests.typing.composition.positive import Application
from tests.typing.models import Repository, Service

from pyinject import Provide, Provider, inject


@inject
def process(item: str, *, service: Service = Provide[Application.service]) -> Repository:
    return service.repo


@inject
async def async_process(item: str, *, service: Service = Provide[Application.service]) -> Repository:
    return service.repo


@inject
def select(key: str, choose: Callable[[str], Service] = Provide[AggregateApplication.service]) -> Service:
    return choose(key)


assert_type(process("item"), Repository)
assert_type(process("item", service=Service(Repository("memory:"))), Repository)
assert_type(Provide[Application.service], Service)
assert_type(Provider[Application.service](), Service)
assert_type(Provider[AggregateApplication.service](), Callable[[str], Service])
assert_type(select("primary"), Service)


async def verify_async() -> None:
    assert_type(await async_process("item"), Repository)


app = Application()
app.wire(modules=[sys.modules[__name__]])
app.unwire()
