
In Clean Architecture, the structure consists of three main layers:

1. **Core** : This layer contains the business logic, data models (entities), and anything related to the core functionality of the application.
2. **Infrastructure** : Responsible for interacting with external systems like databases, email services, or SMS providers.
3. **Presentation** : This layer is responsible for presenting the data, and can be implemented using various frameworks or methods like MVC, Web API, GraphQL, etc.

The key idea behind Clean Architecture is that these layers are separated so that the core business logic can remain independent of how the data is presented or how the external systems interact with the application. This makes the code more modular, maintainable, and testable. The core logic can be reused across different presentation formats without any changes, allowing flexibility in how the application is deployed.


### Key Points About Clean Architecture:

1. **Purpose of Clean Architecture**
   * It standardizes project structure so that multiple developers can collaborate efficiently.
   * Helps in organizing code into clear, maintainable layers.
2. **Problem It Solves**
   * Prevents disorganized code when multiple self-taught developers work together.
   * Ensures consistency by defining where different parts of the code should be placed.
3. **Main Layers of Clean Architecture**
   * **Core (Business Logic & Entities)** : Contains the application's business logic and data models (entities).
   * **Infrastructure** : Handles external dependencies like databases, third-party services, and APIs.
   * **Presentation** : Manages how data is presented to users, which can be via MVC, Web API, GraphQL, etc.
4. **Separation of Concerns**
   * Business logic is independent of external dependencies.
   * The presentation layer can be swapped without modifying business logic (e.g., using Web API, GraphQL, or gRPC).
5. **Project Structure**
   * **SRC Folder** : Contains the main application code.
   * **Tests Folder** : Contains unit and integration tests.
   * Folders are manually created to ensure real separation and maintain structure in Git repositories.
6. **Flexibility & Scalability**
   * Enables different frontends (mobile, web, CLI) to interact with the same backend logic.
   * Encourages modular design for easier maintenance and updates.
7. **Not a New Coding Language or Syntax**
   * Uses the same programming concepts but structures them differently.
   * Helps in maintaining clear separation between different functionalities.
