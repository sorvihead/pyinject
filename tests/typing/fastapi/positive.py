from typing import Annotated, assert_type

from fastapi import APIRouter, Depends
from tests.typing.composition.positive import Application
from tests.typing.models import Repository, Service

from pyinject import Provider, inject

router = APIRouter()


@router.get("/items")
@inject
def endpoint(service: Annotated[Service, Depends(Provider[Application.service])]) -> str:
    assert_type(service, Service)
    return service.repo.dsn


@router.get("/async-items")
@inject
async def async_endpoint(service: Annotated[Service, Depends(Provider[Application.service])]) -> str:
    assert_type(service, Service)
    return service.repo.dsn


assert_type(Provider[Application.service](), Service)
assert_type(endpoint(Service(Repository("memory:"))), str)


async def check_async_endpoint() -> None:
    assert_type(await async_endpoint(Service(Repository("memory:"))), str)


# Deliberate checker blind spot: Annotated metadata does not constrain Service.
@router.get("/metadata-mismatch")
@inject
def metadata_mismatch(service: Annotated[Repository, Depends(Provider[Application.service])]) -> str:
    assert_type(service, Repository)
    return service.dsn
