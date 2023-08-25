# Introduction to Clean Architecture

Clean Architecture emphasizes a clear separation of concerns and a layered approach to designing applications. It consists of different layers, each serving a specific purpose:

- Entities: Represent the core business logic and data structures.
- Use Cases: Contain the application's business rules and orchestrate the flow of data between entities and external systems.
- Interface Adapters: Convert data between the use cases and the external world (e.g., frameworks, controllers, presenters).
- Frameworks & Drivers: Consist of external tools and frameworks used to connect the application to the outside world (e.g., web frameworks, databases).

## How to Install

1. Make sure you have Poetry installed.
2. Clone this repository.
3. Navigate to the project directory.
4. To ensure you are using the correct Python version, refer to the .python-version file in the project directory.
5. To install the project dependencies using Poetry, run:
```
poetry install
```

This will create a virtual environment and install the required dependencies.

## Usage

After installing the dependencies, you can first test the applications:
```
poetry run pytest
```

Try to expand the use cases, and then create an API that uses it.

Feel free to explore the project's code to better understand how Clean Architecture principles are applied in a Python context. If you have any questions or suggestions, please don't hesitate to reach out to me.

Disclaimer: This is a simplified example for educational purposes and might not cover all aspects of a real-world application.