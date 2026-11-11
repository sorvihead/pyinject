"""Type-only FastAPI example. Real integration tests belong to U11."""

import sys
from typing import Annotated

from examples.application import Application
from examples.domain import Service
from fastapi import APIRouter, Depends, FastAPI

from pyinject import Provider, inject

router = APIRouter()


@router.get("/items")
@inject
def items(service: Annotated[Service, Depends(Provider[Application.service])]) -> str:
    return service.repo.dsn


@router.get("/async-items")
@inject
async def async_items(service: Annotated[Service, Depends(Provider[Application.service])]) -> str:
    return service.repo.dsn


def configure() -> tuple[FastAPI, Application]:
    container = Application()
    container.wire(modules=[sys.modules[__name__]])
    api = FastAPI()
    api.include_router(router)
    return api, container
