"""Type-only example of default-marker injection and module wiring."""

import sys

from examples.application import Application
from examples.domain import Service

from pyinject import Provide, inject


@inject
def process(item: str, *, service: Service = Provide[Application.service]) -> str:
    return f"{item}: {service.repo.dsn}"


@inject
async def async_process(item: str, *, service: Service = Provide[Application.service]) -> str:
    return f"{item}: {service.repo.dsn}"


def configure() -> Application:
    container = Application()
    container.wire(modules=[sys.modules[__name__]])
    return container
