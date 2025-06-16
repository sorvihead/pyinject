"""Advanced example demonstrating more PyInject features."""

from typing import Protocol

from pyinject import Container


class IEmailService(Protocol):
    """Email service interface."""
    
    def send_email(self, to: str, subject: str, body: str) -> bool:
        """Send an email."""
        ...


class ILogger(Protocol):
    """Logger interface."""
    
    def log(self, level: str, message: str) -> None:
        """Log a message."""
        ...


# Concrete implementations
class ConsoleLogger:
    """Logger that outputs to console."""
    
    def log(self, level: str, message: str) -> None:
        """Log a message to console."""
        print(f"[{level.upper()}] {message}")


class SmtpEmailService:
    """SMTP email service implementation."""
    
    def __init__(self, logger: ConsoleLogger) -> None:
        self.logger = logger
        self.logger.log("info", "SMTP Email Service initialized")
    
    def send_email(self, to: str, subject: str, body: str) -> bool:
        """Send email via SMTP."""
        self.logger.log("info", f"Sending email to {to}: {subject}")
        # Simulate sending email
        return True


class MockEmailService:
    """Mock email service for testing."""
    
    def __init__(self, logger: ConsoleLogger) -> None:
        self.logger = logger
        self.sent_emails: list[dict[str, str]] = []
        self.logger.log("info", "Mock Email Service initialized")
    
    def send_email(self, to: str, subject: str, body: str) -> bool:
        """Mock sending email."""
        self.sent_emails.append({"to": to, "subject": subject, "body": body})
        self.logger.log("info", f"Mock email sent to {to}: {subject}")
        return True


class NotificationService:
    """Service that sends notifications via email."""
    
    def __init__(self, email_service: SmtpEmailService, logger: ConsoleLogger) -> None:
        self.email_service = email_service
        self.logger = logger
        self.logger.log("info", "Notification Service initialized")
    
    def notify_user(self, user_email: str, message: str) -> bool:
        """Send notification to user."""
        subject = "System Notification"
        return self.email_service.send_email(user_email, subject, message)


class UserManager:
    """Manages user operations."""
    
    def __init__(self, notification_service: NotificationService, logger: ConsoleLogger) -> None:
        self.notification_service = notification_service
        self.logger = logger
        self.logger.log("info", "User Manager initialized")
    
    def create_user(self, email: str, name: str) -> bool:
        """Create a new user."""
        self.logger.log("info", f"Creating user: {name} ({email})")
        
        # Send welcome notification
        welcome_message = f"Welcome {name}! Your account has been created successfully."
        success = self.notification_service.notify_user(email, welcome_message)
        
        if success:
            self.logger.log("info", f"User {name} created and notified successfully")
        else:
            self.logger.log("error", f"Failed to notify user {name}")
        
        return success


def demo_basic_usage() -> None:
    """Demonstrate basic usage with different implementations."""
    print("=== Demo 1: Basic Usage with SMTP ===\n")
    
    container = Container()
    
    # Register services with concrete types
    container.register(ConsoleLogger, lifetime="singleton")
    container.register(SmtpEmailService, lifetime="singleton")
    container.register(NotificationService)
    container.register(UserManager)
    
    # Resolve and use
    user_manager = container.resolve(UserManager)
    user_manager.create_user("john@example.com", "John Doe")


def demo_interface_binding() -> None:
    """Demonstrate interface-based registration."""
    print("\n=== Demo 2: Interface-based Registration ===\n")
    
    container = Container()
    
    # Register interfaces to concrete implementations
    container.register(ILogger, ConsoleLogger, lifetime="singleton")
    container.register(IEmailService, MockEmailService, lifetime="singleton")  
    container.register(NotificationService)
    container.register(UserManager)
    
    # Resolve and use
    user_manager = container.resolve(UserManager)
    user_manager.create_user("jane@example.com", "Jane Smith")
    
    # Access the mock email service to check sent emails
    email_service = container.resolve(IEmailService)
    if isinstance(email_service, MockEmailService):
        print(f"\nMock Email Service sent {len(email_service.sent_emails)} emails:")
        for email in email_service.sent_emails:
            print(f"  - To: {email['to']}, Subject: {email['subject']}")


def demo_named_services() -> None:
    """Demonstrate named service registration."""
    print("\n=== Demo 3: Named Services ===\n")
    
    container = Container()
    
    # Register multiple implementations with names
    container.register(ILogger, ConsoleLogger, name="console", lifetime="singleton")
    container.register(IEmailService, SmtpEmailService, name="smtp")
    container.register(IEmailService, MockEmailService, name="mock")
    
    # Use factory to choose email service based on environment
    def notification_factory() -> NotificationService:
        logger = container.resolve(ILogger, name="console")
        # In real app, this could be based on config/environment
        email_service = container.resolve(IEmailService, name="mock")
        return NotificationService(email_service, logger)
    
    container.register_factory(NotificationService, notification_factory)
    
    # Register UserManager with specific logger
    def user_manager_factory() -> UserManager:
        notification_service = container.resolve(NotificationService)
        logger = container.resolve(ILogger, name="console")
        return UserManager(notification_service, logger)
    
    container.register_factory(UserManager, user_manager_factory)
    
    # Resolve and use
    user_manager = container.resolve(UserManager)
    user_manager.create_user("admin@example.com", "Admin User")


def demo_factory_registration() -> None:
    """Demonstrate factory-based registration."""
    print("\n=== Demo 4: Factory Registration ===\n")
    
    container = Container()
    
    # Register logger factory that creates configured loggers
    def create_configured_logger() -> ConsoleLogger:
        logger = ConsoleLogger()
        # Could add configuration here
        return logger
    
    # Register email service factory with configuration
    def create_email_service() -> MockEmailService:
        logger = container.resolve(ILogger)
        service = MockEmailService(logger)
        # Could add configuration here
        return service
    
    container.register_factory(ILogger, create_configured_logger, lifetime="singleton")
    container.register_factory(IEmailService, create_email_service, lifetime="singleton")
    container.register(NotificationService)
    container.register(UserManager)
    
    # Resolve and use
    user_manager = container.resolve(UserManager)
    user_manager.create_user("factory@example.com", "Factory User")


def main() -> None:
    """Run all demos."""
    print("=== PyInject Advanced Examples ===\n")
    
    demo_basic_usage()
    demo_interface_binding()
    demo_named_services()
    demo_factory_registration()
    
    print("\n=== All demos completed successfully! ===")


if __name__ == "__main__":
    main()
