"""Type definitions and protocols for PyInject DI framework."""

from typing import Any, Callable, Literal, Protocol

type ServiceLifetime = Literal["singleton", "transient"]
type ServiceKey = type[Any] | str
type ServiceFactory[T] = Callable[[], T]
type ServiceImplementation[T] = type[T] | ServiceFactory[T] | T


class Injectable(Protocol):
    """Protocol for classes that can be injected by the DI container."""

    def __init__(self, /, *args: object, **kwargs: object) -> None:
        """Initialize the injectable class."""
        ...


class ServiceDescriptor[T]:
    """Describes how a service should be created and managed by the container."""

    def __init__(
        self,
        service_type: type[T],
        implementation: ServiceImplementation[T],
        lifetime: ServiceLifetime,
        name: str | None = None,
    ) -> None:
        self.service_type = service_type
        self.implementation = implementation
        self.lifetime = lifetime
        self.name = name
        self._instance: T | None = None

    def is_singleton(self) -> bool:
        """Check if this service is registered as singleton."""
        return self.lifetime == "singleton"

    def has_instance(self) -> bool:
        """Check if singleton instance is already created."""
        return self._instance is not None

    def get_instance(self) -> T | None:
        """Get the singleton instance if available."""
        return self._instance

    def set_instance(self, instance: T) -> None:
        """Set the singleton instance."""
        self._instance = instance
