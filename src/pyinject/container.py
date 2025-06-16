"""Core dependency injection container implementation."""

import inspect
from typing import Any, TypeIs, get_type_hints, overload

from .exceptions import CircularDependencyError, InvalidRegistrationError, ServiceNotFoundError
from .types import ServiceDescriptor, ServiceFactory, ServiceKey, ServiceLifetime


class Container:
    """Main dependency injection container that manages service registration and resolution."""

    def __init__(self) -> None:
        self._services: dict[ServiceKey, ServiceDescriptor] = {}
        self._resolution_stack: list[type] = []

    @overload
    def register[T](
        self,
        service_type: type[T],
        implementation: None = None,
        *,
        lifetime: ServiceLifetime = "transient",
        name: str | None = None,
    ) -> None:
        """Register a service type to itself."""
        ...

    @overload
    def register[T](
        self,
        service_type: type[T],
        implementation: type[T],
        *,
        lifetime: ServiceLifetime = "transient",
        name: str | None = None,
    ) -> None:
        """Register a service type to a concrete implementation class."""
        ...

    @overload
    def register[T](
        self,
        service_type: type[T],
        implementation: ServiceFactory[T],
        *,
        lifetime: ServiceLifetime = "transient",
        name: str | None = None,
    ) -> None:
        """Register a service type to a factory function."""
        ...

    def register[T](
        self,
        service_type: type[T],
        implementation: type[T] | ServiceFactory[T] | None = None,
        *,
        lifetime: ServiceLifetime = "transient",
        name: str | None = None,
    ) -> None:
        """Register a service with its implementation.

        Args:
            service_type: The interface or base type to register
            implementation: The concrete implementation, factory, or None (defaults to service_type)
            lifetime: Service lifetime (singleton or transient)
            name: Optional service name for named registration

        Raises:
            InvalidRegistrationError: If registration parameters are invalid
        """
        if implementation is None:
            implementation = service_type

        key = self._create_service_key(service_type, name)
        descriptor = ServiceDescriptor(service_type, implementation, lifetime, name)
        self._services[key] = descriptor

    def register_instance[T](
        self,
        service_type: type[T],
        instance: T,
        name: str | None = None,
    ) -> None:
        """Register a specific instance as a singleton service.

        Args:
            service_type: The interface or base type to register
            instance: The instance to register
            name: Optional service name for named registration
        """
        key = self._create_service_key(service_type, name)
        descriptor = ServiceDescriptor(service_type, instance, "singleton", name)
        descriptor.set_instance(instance)
        self._services[key] = descriptor

    def register_factory[T](
        self,
        service_type: type[T],
        factory: ServiceFactory[T],
        lifetime: ServiceLifetime = "transient",
        name: str | None = None,
    ) -> None:
        """Register a factory function for creating service instances.

        Args:
            service_type: The interface or base type to register
            factory: Factory function that creates service instances
            lifetime: Service lifetime (singleton or transient)
            name: Optional service name for named registration
        """
        key = self._create_service_key(service_type, name)
        descriptor = ServiceDescriptor(service_type, factory, lifetime, name)
        self._services[key] = descriptor

    def resolve[T](self, service_type: type[T], name: str | None = None) -> T:
        """Resolve a service instance from the container.

        Args:
            service_type: The type of service to resolve
            name: Optional service name for named resolution

        Returns:
            An instance of the requested service type

        Raises:
            ServiceNotFoundError: If the service is not registered
            CircularDependencyError: If circular dependency is detected
        """
        key = self._create_service_key(service_type, name)

        if key not in self._services:
            raise ServiceNotFoundError(service_type, name)

        descriptor = self._services[key]
        # Cast to proper generic type for type safety
        typed_descriptor: ServiceDescriptor[T] = descriptor  # type: ignore[assignment]

        # Return existing singleton instance if available
        if typed_descriptor.is_singleton() and typed_descriptor.has_instance():
            instance = typed_descriptor.get_instance()
            if instance is not None:
                return instance

        # Check for circular dependency
        if service_type in self._resolution_stack:
            self._resolution_stack.append(service_type)
            raise CircularDependencyError(self._resolution_stack.copy())

        # Add to resolution stack for circular dependency detection
        self._resolution_stack.append(service_type)

        try:
            instance = self._create_instance(typed_descriptor)

            # Store singleton instance
            if typed_descriptor.is_singleton():
                typed_descriptor.set_instance(instance)

            return instance
        finally:
            # Remove from resolution stack
            self._resolution_stack.pop()

    def _create_instance[T](self, descriptor: ServiceDescriptor[T]) -> T:
        """Create an instance based on the service descriptor."""
        implementation = descriptor.implementation

        # Handle direct instance (pre-created object)
        if not inspect.isclass(implementation) and not callable(implementation):
            if self._obj_type_guard(implementation, descriptor.service_type):
                return implementation

        # Handle factory function
        if callable(implementation) and not inspect.isclass(implementation):
            result = implementation()
            if self._obj_type_guard(result, descriptor.service_type):
                return result

        # Handle class instantiation with dependency injection
        if inspect.isclass(implementation):
            instance = self._create_class_instance(implementation)
            if self._obj_type_guard(instance, descriptor.service_type):
                return instance

        raise InvalidRegistrationError(f"Cannot create instance from {implementation}")

    def _obj_type_guard[T](self, obj: object, target_type: type[T]) -> TypeIs[T]:
        """
        Cast object to type T.

        This is used for runtime type conversion where type safety is guaranteed by design.
        The type checker cannot verify this at compile time, but our DI container logic
        ensures that the object is of the correct type at runtime.
        """
        return isinstance(obj, target_type)

    def _create_class_instance[T](self, cls: type[T]) -> T:
        """Create a class instance with automatic dependency injection."""
        try:
            # Get constructor signature
            signature = inspect.signature(cls.__init__)
            type_hints = get_type_hints(cls.__init__)

            # Prepare constructor arguments
            kwargs: dict[str, Any] = {}

            for param_name, param in signature.parameters.items():
                # Skip 'self' parameter
                if param_name == "self":
                    continue

                # Get parameter type from type hints
                if param_name in type_hints:
                    param_type = type_hints[param_name]

                    # Skip non-class types for now (basic types, etc.)
                    if inspect.isclass(param_type):
                        kwargs[param_name] = self.resolve(param_type)
                elif param.default is not param.empty:
                    # Parameter has default value, skip injection
                    continue
                else:
                    # Parameter without type hint and no default value
                    # For now, we'll skip it but this could be enhanced
                    pass

            instance = cls(**kwargs)
            if self._obj_type_guard(instance, cls):
                return instance
            raise InvalidRegistrationError(f"Created instance is not of type {cls.__name__}")

        except CircularDependencyError:
            # Re-raise circular dependency errors as-is
            raise
        except Exception as e:
            raise InvalidRegistrationError(f"Failed to create instance of {cls.__name__}: {e}") from e

    def _create_service_key(self, service_type: type, name: str | None) -> ServiceKey:
        """Create a unique key for service registration."""
        if name is None:
            return service_type
        return f"{service_type.__name__}:{name}"

    def is_registered(self, service_type: type, name: str | None = None) -> bool:
        """Check if a service is registered in the container."""
        key = self._create_service_key(service_type, name)
        return key in self._services

    def clear(self) -> None:
        """Clear all registered services from the container."""
        self._services.clear()
        self._resolution_stack.clear()
