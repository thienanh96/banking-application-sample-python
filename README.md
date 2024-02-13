### `main.py` Overview

The `main.py` file serves as the entry point to the Banking System application, orchestrating the overall flow and interactions between different layers of the application in accordance with Clean Architecture principles. Its primary responsibilities include initializing the application's environment, setting up dependencies, and providing a user interface for interaction with the system.

#### Key Features

- **Initialization**: `main.py` initializes the application by setting up the necessary configurations, including environment variables, application settings, and logging. This ensures that the application has all the required context and settings to operate correctly.

- **Dependency Injection**: It establishes the dependencies between the application's layers. This includes instantiating the infrastructure components (e.g., database connections, repository implementations) and injecting these instances into the application services and use cases. This approach decouples the application's core logic from specific implementations, enhancing modularity and testability.
