from typing import assert_type

from examples.application import Application
from examples.domain import Repository, Service

from pyinject import DeclarativeContainer, Provide, Provider, inject, providers
from pyinject.containers import DeclarativeContainer as ContainerAlias
from pyinject.exceptions import (
    CircularDependencyError,
    InvalidContainerError,
    InvalidGraphError,
    PyInjectError,
    ResolutionError,
    UnboundProviderError,
    UnknownFactoryError,
    UnreachableProviderError,
    UnwiredError,
    WiringConflictError,
)
from pyinject.wiring import Provide as ProvideAlias

assert_type(Application().service(), Service)
assert_type(Application.repository.ref, Repository)
assert_type(Provide[Application.service], Service)
assert_type(ProvideAlias[Application.service], Service)
assert_type(Provider[Application.service](), Service)
assert_type(ContainerAlias(), DeclarativeContainer)


@inject
def identity(service: Service) -> Service:
    return service


def errors() -> list[type[PyInjectError]]:
    return [
        InvalidContainerError,
        InvalidGraphError,
        UnboundProviderError,
        CircularDependencyError,
        ResolutionError,
        UnknownFactoryError,
        UnreachableProviderError,
        UnwiredError,
        WiringConflictError,
    ]


def reference(value: providers.Ref[Service]) -> providers.Ref[Service]:
    return value
