"""Basic example demonstrating PyInject usage."""

from pyinject import Container


# Define some example services
class DatabaseConfig:
    """Configuration for database connection."""
    
    def __init__(self) -> None:
        self.connection_string = "sqlite:///example.db"
        self.timeout = 30


class Logger:
    """Simple logging service."""
    
    def log(self, message: str) -> None:
        """Log a message."""
        print(f"[LOG] {message}")


class Database:
    """Database service that depends on config and logger."""
    
    def __init__(self, config: DatabaseConfig, logger: Logger) -> None:
        self.config = config
        self.logger = logger
        self.logger.log(f"Database initialized with {config.connection_string}")
    
    def query(self, sql: str) -> str:
        """Execute a query."""
        self.logger.log(f"Executing query: {sql}")
        return "Query results"


class UserService:
    """User service that depends on database."""
    
    def __init__(self, database: Database, logger: Logger) -> None:
        self.database = database
        self.logger = logger
        self.logger.log("UserService initialized")
    
    def get_user(self, user_id: int) -> str:
        """Get user by ID."""
        result = self.database.query(f"SELECT * FROM users WHERE id = {user_id}")
        self.logger.log(f"Retrieved user {user_id}")
        return f"User {user_id} data: {result}"


def main() -> None:
    """Demonstrate basic dependency injection."""
    print("=== PyInject Basic Example ===\n")
    
    # Create container
    container = Container()
    
    # Register services
    print("1. Registering services...")
    container.register(DatabaseConfig, lifetime="singleton")  # Singleton config
    container.register(Logger, lifetime="singleton")  # Singleton logger
    container.register(Database, lifetime="singleton")  # Singleton database
    container.register(UserService)  # Transient user service
    
    print("   ✓ All services registered\n")
    
    # Resolve and use services
    print("2. Resolving UserService (will trigger dependency chain)...")
    user_service = container.resolve(UserService)
    
    print("\n3. Using the resolved service...")
    result = user_service.get_user(123)
    print(f"   Result: {result}\n")
    
    # Demonstrate singleton behavior
    print("4. Demonstrating singleton behavior...")
    user_service2 = container.resolve(UserService)
    print(f"   Same logger instance? {user_service.logger is user_service2.logger}")
    print(f"   Same database instance? {user_service.database is user_service2.database}")
    print(f"   Same user service instance? {user_service is user_service2}")
    
    print("\n=== Example completed successfully! ===")


if __name__ == "__main__":
    main()
