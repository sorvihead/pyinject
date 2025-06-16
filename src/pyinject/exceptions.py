"""Exception classes for PyInject DI framework."""


class DIError(Exception):
    """Base exception for all dependency injection errors."""

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


class ServiceNotFoundError(DIError):
    """Raised when a requested service is not registered in the container."""

    def __init__(self, service_type: type, name: str | None = None) -> None:
        service_name = f"{service_type.__name__}" + (f" (name: {name})" if name else "")
        super().__init__(f"Service not found: {service_name}")
        self.service_type = service_type
        self.service_name = name


class CircularDependencyError(DIError):
    """Raised when a circular dependency is detected during service resolution."""

    def __init__(self, dependency_chain: list[type]) -> None:
        chain_names = " -> ".join(cls.__name__ for cls in dependency_chain)
        super().__init__(f"Circular dependency detected: {chain_names}")
        self.dependency_chain = dependency_chain


class InvalidRegistrationError(DIError):
    """Raised when attempting to register a service with invalid parameters."""

    def __init__(self, message: str) -> None:
        super().__init__(f"Invalid registration: {message}")
