"""Test the improved type system with overloaded methods."""

from pyinject import Container


class Logger:
    def log(self, message: str) -> None:
        print(f"[LOG] {message}")


class EmailService:
    def __init__(self, logger: Logger) -> None:
        self.logger = logger


def email_factory() -> EmailService:
    logger = Logger()
    return EmailService(logger)


def main() -> None:
    """Test overloaded register methods."""
    container = Container()
    
    # Test 1: Register service type to itself
    container.register(Logger)  # Type: Logger -> Logger
    
    # Test 2: Register service type to concrete implementation
    container.register(EmailService, EmailService)  # Type: EmailService -> EmailService
    
    # Test 3: Register service type to factory function
    container.register(EmailService, email_factory, name="factory")  # Type: EmailService -> factory
    
    # Test resolution
    logger = container.resolve(Logger)  # Should return Logger
    email_service = container.resolve(EmailService)  # Should return EmailService  
    factory_email = container.resolve(EmailService, name="factory")  # Should return EmailService
    
    print(f"Logger type: {type(logger)}")
    print(f"Email service type: {type(email_service)}")
    print(f"Factory email type: {type(factory_email)}")
    
    # Test type safety - these should work with proper IDE intellisense
    logger.log("Test message")
    email_service.logger.log("Another message")
    factory_email.logger.log("Factory message")
    
    print("All type tests passed!")


if __name__ == "__main__":
    main()
