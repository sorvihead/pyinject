"""Test cases for the Container class."""

import pytest

from pyinject import CircularDependencyError, Container, InvalidRegistrationError, ServiceNotFoundError


class MockService:
    """Mock service for testing."""
    
    def __init__(self) -> None:
        self.value = "test"


class MockDependentService:
    """Mock service that depends on another service."""
    
    def __init__(self, dependency: MockService) -> None:
        self.dependency = dependency


class MockCircularA:
    """Mock service for circular dependency testing."""
    
    def __init__(self, b: "MockCircularB") -> None:
        self.b = b


class MockCircularB:
    """Mock service for circular dependency testing."""
    
    def __init__(self, a: MockCircularA) -> None:
        self.a = a


class TestContainer:
    """Test cases for Container class."""
    
    def setup_method(self) -> None:
        """Set up test container for each test."""
        self.container = Container()
    
    def test_register_and_resolve_simple_service(self) -> None:
        """Test basic service registration and resolution."""
        self.container.register(MockService)
        
        service = self.container.resolve(MockService)
        
        assert isinstance(service, MockService)
        assert service.value == "test"
    
    def test_register_and_resolve_with_dependencies(self) -> None:
        """Test service resolution with automatic dependency injection."""
        self.container.register(MockService)
        self.container.register(MockDependentService)
        
        service = self.container.resolve(MockDependentService)
        
        assert isinstance(service, MockDependentService)
        assert isinstance(service.dependency, MockService)
    
    def test_singleton_lifetime(self) -> None:
        """Test singleton service lifetime."""
        self.container.register(MockService, lifetime="singleton")
        
        service1 = self.container.resolve(MockService)
        service2 = self.container.resolve(MockService)
        
        assert service1 is service2
    
    def test_transient_lifetime(self) -> None:
        """Test transient service lifetime."""
        self.container.register(MockService, lifetime="transient")
        
        service1 = self.container.resolve(MockService)
        service2 = self.container.resolve(MockService)
        
        assert service1 is not service2  
        assert isinstance(service1, MockService)
        assert isinstance(service2, MockService)
    
    def test_register_instance(self) -> None:
        """Test registering a specific instance."""
        instance = MockService()
        instance.value = "custom"
        
        self.container.register_instance(MockService, instance)
        
        resolved = self.container.resolve(MockService)
        
        assert resolved is instance
        assert resolved.value == "custom"
    
    def test_register_factory(self) -> None:
        """Test registering a factory function."""
        def factory() -> MockService:
            service = MockService()
            service.value = "factory_created"
            return service
        
        self.container.register_factory(MockService, factory)
        
        service = self.container.resolve(MockService)
        
        assert isinstance(service, MockService)
        assert service.value == "factory_created"
    
    def test_named_registration(self) -> None:
        """Test named service registration."""
        self.container.register(MockService, name="service1")
        self.container.register(MockService, name="service2")
        
        service1 = self.container.resolve(MockService, name="service1")
        service2 = self.container.resolve(MockService, name="service2")
        
        assert isinstance(service1, MockService)
        assert isinstance(service2, MockService)
        assert service1 is not service2
    
    def test_service_not_found_error(self) -> None:
        """Test ServiceNotFoundError is raised for unregistered services."""
        with pytest.raises(ServiceNotFoundError) as exc_info:
            self.container.resolve(MockService)
        
        assert "MockService" in str(exc_info.value)
    
    def test_circular_dependency_detection(self) -> None:
        """Test circular dependency detection."""
        self.container.register(MockCircularA)
        self.container.register(MockCircularB)
        
        with pytest.raises(CircularDependencyError) as exc_info:
            self.container.resolve(MockCircularA)
        
        assert "Circular dependency detected" in str(exc_info.value)
        assert "MockCircularA" in str(exc_info.value)
        assert "MockCircularB" in str(exc_info.value)
    
    def test_invalid_registration_error(self) -> None:
        """Test InvalidRegistrationError for invalid implementations."""
        with pytest.raises(InvalidRegistrationError):
            self.container.register(MockService, "not_a_class")  # type: ignore[arg-type]
    
    def test_is_registered(self) -> None:
        """Test service registration checking."""
        assert not self.container.is_registered(MockService)
        
        self.container.register(MockService)
        
        assert self.container.is_registered(MockService)
        assert not self.container.is_registered(MockService, name="test")
        
        self.container.register(MockService, name="test")
        
        assert self.container.is_registered(MockService, name="test")
    
    def test_clear_container(self) -> None:
        """Test clearing all services from container."""
        self.container.register(MockService)
        assert self.container.is_registered(MockService)
        
        self.container.clear()
        
        assert not self.container.is_registered(MockService)
        with pytest.raises(ServiceNotFoundError):
            self.container.resolve(MockService)
