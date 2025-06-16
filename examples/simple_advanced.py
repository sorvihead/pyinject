"""Simple advanced example demonstrating PyInject features."""

from pyinject import Container


class Logger:
    """Simple console logger."""
    
    def log(self, level: str, message: str) -> None:
        """Log a message to console."""
        print(f"[{level.upper()}] {message}")


class DatabaseConfig:
    """Database configuration."""
    
    def __init__(self) -> None:
        self.connection_string = "postgresql://localhost:5432/mydb"
        self.timeout = 30


class EmailService:
    """Email service."""
    
    def __init__(self, logger: Logger) -> None:
        self.logger = logger
        self.sent_emails: list[dict[str, str]] = []
        self.logger.log("info", "Email Service initialized")
    
    def send_email(self, to: str, subject: str, body: str) -> bool:
        """Send an email."""
        self.sent_emails.append({"to": to, "subject": subject, "body": body})
        self.logger.log("info", f"Email sent to {to}: {subject}")
        return True


class UserService:
    """Main user service."""
    
    def __init__(self, email_service: EmailService, config: DatabaseConfig, logger: Logger) -> None:
        self.email_service = email_service
        self.config = config
        self.logger = logger
        self.logger.log("info", f"User Service initialized with {config.connection_string}")
    
    def register_user(self, email: str, name: str) -> bool:
        """Register a new user."""
        self.logger.log("info", f"Registering user: {name} ({email})")
        
        # Send welcome email
        subject = "Welcome!"
        body = f"Hello {name}, welcome to our service!"
        success = self.email_service.send_email(email, subject, body)
        
        if success:
            self.logger.log("info", f"User {name} registered successfully")
        else:
            self.logger.log("error", f"Failed to register user {name}")
        
        return success


def demo_basic() -> None:
    """Basic dependency injection demo."""
    print("=== Basic Dependency Injection ===\n")
    
    container = Container()
    
    # Register services
    container.register(Logger, lifetime="singleton")
    container.register(DatabaseConfig, lifetime="singleton")
    container.register(EmailService, lifetime="singleton")
    container.register(UserService)
    
    # Resolve and use
    user_service = container.resolve(UserService)
    user_service.register_user("test@example.com", "Test User")
    
    # Show emails
    email_service = container.resolve(EmailService)
    print(f"\nEmails sent: {len(email_service.sent_emails)}")


def demo_factories() -> None:
    """Factory registration demo."""
    print("\n=== Factory Registration ===\n")
    
    container = Container()
    
    # Factory for custom config
    def create_config() -> DatabaseConfig:
        config = DatabaseConfig()
        config.connection_string = "sqlite:///test.db"
        return config
    
    container.register(Logger, lifetime="singleton")
    container.register_factory(DatabaseConfig, create_config, lifetime="singleton")
    container.register(EmailService, lifetime="singleton")
    container.register(UserService)
    
    user_service = container.resolve(UserService)
    user_service.register_user("factory@example.com", "Factory User")


def demo_named() -> None:
    """Named services demo."""
    print("\n=== Named Services ===\n")
    
    container = Container()
    
    # Multiple configs
    def dev_config() -> DatabaseConfig:
        config = DatabaseConfig()
        config.connection_string = "sqlite:///dev.db"
        return config
    
    def prod_config() -> DatabaseConfig:
        config = DatabaseConfig()
        config.connection_string = "postgresql://prod:5432/db"
        return config
    
    container.register(Logger, lifetime="singleton")
    container.register_factory(DatabaseConfig, dev_config, name="dev")
    container.register_factory(DatabaseConfig, prod_config, name="prod")
    
    # Resolve specific configs
    dev_cfg = container.resolve(DatabaseConfig, name="dev")
    prod_cfg = container.resolve(DatabaseConfig, name="prod")
    
    print(f"Dev config: {dev_cfg.connection_string}")
    print(f"Prod config: {prod_cfg.connection_string}")


def main() -> None:
    """Run all demos."""
    print("=== PyInject Advanced Examples ===\n")
    
    demo_basic()
    demo_factories()
    demo_named()
    
    print("\n=== All examples completed! ===")


if __name__ == "__main__":
    main()
