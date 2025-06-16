# PyInject - Python Dependency Injection Framework

A modern, lightweight dependency injection framework for Python 3.13+ with comprehensive type hints and clean, simple API.

## Features

- 🚀 **Modern Python**: Built for Python 3.13+ with modern syntax and comprehensive type hints
- 🔧 **Constructor Injection**: Automatic dependency injection via type annotations
- 📦 **Multiple Lifetimes**: Support for singleton and transient service lifetimes
- 🏭 **Factory Pattern**: Register services using factory functions
- 🏷️ **Named Services**: Register multiple implementations with names
- 🔍 **Type Safety**: Full type hints and compile-time type checking
- 🎯 **Simple API**: Clean and intuitive registration and resolution API
- 🔄 **Circular Dependency Detection**: Automatic detection and clear error messages
- ⚡ **High Performance**: Optimized for speed with minimal overhead

## Quick Start

### Basic Usage

```python
from pyinject import Container

# Define your services
class Logger:
    def log(self, message: str) -> None:
        print(f"[LOG] {message}")

class EmailService:
    def __init__(self, logger: Logger) -> None:
        self.logger = logger
    
    def send_email(self, to: str, subject: str) -> bool:
        self.logger.log(f"Sending email to {to}: {subject}")
        return True

class UserService:
    def __init__(self, email_service: EmailService, logger: Logger) -> None:
        self.email_service = email_service
        self.logger = logger
    
    def register_user(self, email: str, name: str) -> bool:
        self.logger.log(f"Registering user: {name}")
        return self.email_service.send_email(email, "Welcome!")

# Set up the container
container = Container()
container.register(Logger, lifetime="singleton")
container.register(EmailService, lifetime="singleton") 
container.register(UserService)

# Resolve and use services
user_service = container.resolve(UserService)
user_service.register_user("john@example.com", "John Doe")
```

## Core Concepts

### Service Registration

PyInject supports multiple ways to register services:

#### 1. Type-based Registration

```python
# Register concrete class
container.register(UserService)

# Register with interface binding
container.register(IEmailService, EmailService)

# Register with lifetime management
container.register(Logger, lifetime="singleton")
```

#### 2. Factory Registration

```python
def create_email_service() -> EmailService:
    logger = container.resolve(Logger)
    service = EmailService(logger)
    # Add custom configuration
    return service

container.register_factory(EmailService, create_email_service)
```

#### 3. Instance Registration

```python
# Register pre-created instance
logger = Logger()
container.register_instance(Logger, logger)
```

#### 4. Named Registration

```python
# Register multiple implementations with names
container.register(DatabaseConfig, name="dev", lifetime="singleton")
container.register(DatabaseConfig, name="prod", lifetime="singleton")

# Resolve specific implementation
dev_config = container.resolve(DatabaseConfig, name="dev")
```

### Service Lifetimes

PyInject supports two service lifetimes:

- **`singleton`**: One instance per container (shared)
- **`transient`**: New instance every time (default)

```python
container.register(Logger, lifetime="singleton")     # Shared instance
container.register(UserService, lifetime="transient") # New instance each time
```

### Automatic Dependency Injection

PyInject automatically resolves constructor dependencies using type annotations:

```python
class UserService:
    # Dependencies are automatically injected based on type hints
    def __init__(self, 
                 repository: UserRepository,
                 email_service: EmailService, 
                 logger: Logger) -> None:
        self.repository = repository
        self.email_service = email_service
        self.logger = logger

# No manual wiring needed - dependencies are resolved automatically
user_service = container.resolve(UserService)
```

## Development Status

### Phase 1: Core Framework ✅
- [x] Basic container with service registration/resolution
- [x] Constructor injection via type annotations
- [x] Singleton and transient lifetimes
- [x] Factory and instance registration
- [x] Named services
- [x] Circular dependency detection
- [x] Comprehensive test suite

### Phase 2: Advanced Features (Upcoming)
- [ ] Decorator-based registration (@injectable, @singleton)
- [ ] Property and method injection
- [ ] Configuration-based wiring (YAML/JSON)
- [ ] Async service support

### Phase 3: Performance Optimization (Future)
- [ ] Rust/PyO3 performance optimizations
- [ ] Compiled service resolution
- [ ] Benchmarking suite

## Examples

Run the included examples to see PyInject in action:

```bash
# Basic usage example
PYTHONPATH=src python examples/basic_usage.py

# Advanced patterns example
PYTHONPATH=src python examples/simple_advanced.py
```

## Testing

```bash
# Run all tests
PYTHONPATH=src python -m pytest tests/ -v

# Run with coverage
PYTHONPATH=src python -m pytest tests/ --cov=src/pyinject
```

## Contributing

This project is designed for educational purposes and aims to become a high-quality open source DI framework. Contributions are welcome!

## License

MIT License - see [LICENSE](LICENSE) file for details.