"""PyInject - A modern dependency injection framework for Python."""

from .container import Container
from .exceptions import CircularDependencyError, DIError, InvalidRegistrationError, ServiceNotFoundError
from .types import Injectable, ServiceDescriptor, ServiceFactory, ServiceLifetime

__version__ = "0.1.0"
__all__ = [
    "Container",
    "DIError",
    "ServiceNotFoundError",
    "CircularDependencyError",
    "InvalidRegistrationError",
    "ServiceLifetime",
    "ServiceFactory",
    "ServiceDescriptor",
    "Injectable",
]
