# Employee Onboarding System

A Django-based web application designed to manage the employee onboarding process. This project provides a clean, maintainable, and scalable architecture for handling employee records (Create, Read, Update, Delete).

## 🏗️ Architecture Pattern

This project deviates from the standard Django "Fat Models, Skinny Views" (MVT) pattern. Instead, it implements a **Layered Architecture** (often referred to as the **Service Layer Pattern** or **Clean Architecture** adapted for Django). 

This approach decouples the core business logic from the HTTP framework (Django), making the application significantly easier to test, maintain, and scale as it grows.

### The Layers

1. **Controllers (`controllers/`)**: 
   - Act as the entry point for HTTP requests (replacing traditional Django Views).
   - Responsible *only* for handling HTTP requests, validating input, calling the appropriate Service, and returning an HTTP response (rendering a template or redirecting).
   - They contain **no business logic**.

2. **Requests (`requests/`)**:
   - Handle the validation of incoming HTTP data (e.g., POST data).
   - Typically implemented using Django Forms to ensure the data is clean and valid before it reaches the business logic layer.

3. **DTOs - Data Transfer Objects (`dtos/`)**:
   - Simple data structures (often Python `dataclasses` or standard classes) used to pass data between the Controller layer and the Service layer.
   - They ensure that the Service layer doesn't depend on HTTP-specific objects like `request.POST` or Django Forms.

4. **Services (`services/`)**:
   - The heart of the application. This layer contains all the **business logic** and use cases.
   - Services take DTOs as input, perform necessary operations (like creating an employee, sending emails, calculating salaries), and interact with the database via Models or Selectors.

5. **Selectors (`selectors/`)**:
   - Dedicated to complex database queries and data fetching (Read operations). 
   - While simple queries might live in Services, Selectors keep the Service layer clean by abstracting away complex ORM lookups.

6. **Models (`models/`)**:
   - Standard Django ORM models.
   - They represent the database tables and relationships but are kept "skinny" (devoid of complex business logic).

### Why this pattern?
- **Separation of Concerns:** HTTP logic is separated from business logic.
- **Testability:** You can test Services and DTOs in isolation without needing a mock HTTP request or a web server.
- **Reusability:** Business logic in Services can be called from anywhere (Controllers, Celery tasks, Management commands, APIs) without duplicating code.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package installer)

### Installation & Setup

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd employee-onboarding
   ```

2. **Create and activate a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**:
   *(Assuming Django is the primary dependency)*
   ```bash
   pip install django
   ```

4. **Apply database migrations**:
   Set up the SQLite database and create the necessary tables.
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the application**:
   Open your web browser and navigate to:
   `http://127.0.0.1:8000/` (or the specific route configured for employees, e.g., `http://127.0.0.1:8000/employees/`)

---

## 📁 Project Structure

```text
employee-onboarding/
├── config/                 # Django project configuration (settings, root urls)
├── employees/              # Main application
│   ├── controllers/        # HTTP request handlers (Views)
│   ├── dtos/               # Data Transfer Objects
│   ├── models/             # Database schemas (Django ORM)
│   ├── requests/           # Input validation (Forms)
│   ├── selectors/          # Database read operations
│   ├── services/           # Core business logic (Write operations)
│   └── templates/          # HTML templates for the UI
└── manage.py               # Django command-line utility
```

## 🛠️ Useful Commands

- **Create a superuser** (to access the Django admin panel):
  ```bash
  python manage.py createsuperuser
  ```
- **Make new migrations** (after changing `models.py`):
  ```bash
  python manage.py makemigrations
  ```
- **Open the Django shell** (for testing ORM queries):
  ```bash
  python manage.py shell
  ```
