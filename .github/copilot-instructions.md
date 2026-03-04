# Copilot Instructions — FastAPI Clean Architecture

You are assisting in a Python backend project using **Clean Architecture**.

Follow these rules STRICTLY.

---

## Architecture Overview

The project uses:

* FastAPI (API layer)
* SQLAlchemy (Infrastructure layer)
* Pydantic (Schemas)
* MySQL database
* Clean Architecture principles

Folder structure:

```
app/
├── api/                # API layer (FastAPI routes)
├── application         # Application layer (use cases, services)
├── core/              # Core utilities (config, database, session)
├── domain/            # Domain layer (domain models, interfaces)
├── infrastructure     # Infrastructure layer (database models, seeders, repositories)
├── migrations         # Database migrations (Alembic)
```

DEPENDENCY RULE:

Outer layers may depend on inner layers.
Inner layers MUST NEVER depend on outer layers.

Domain must NOT import:

* fastapi
* sqlalchemy
* pydantic
* mysql drivers

---
## Coding Rules

### 1. API Layer

* No business logic
* Call use cases only
* Use dependency injection
* Return response schemas

### 2. Domain Layer

* Pure Python classes
* No framework imports
* Repository interfaces defined using ABC

### 3. Application Layer

* Contains business logic
* Use cases orchestrate repositories
* No SQLAlchemy usage

### 4. Infrastructure Layer

* SQLAlchemy models live here
* Repository implementations live here
* Convert ORM models ↔ domain entities

---

## Naming Conventions

Entity:
User

SQLAlchemy Model:
UserModel

Repository Interface:
UserRepository

Repository Implementation:
UserRepositoryImpl

Use Case:
CreateUser
GetUser
UpdateUser

Route file:
users.py

---

## Use Case Pattern

Each use case must:

* Be a class
* Accept repositories via constructor
* Expose execute() method

Example:

class CreateUser:
def **init**(self, repo: UserRepository):
self.repo = repo

```
def execute(self, data):
    ...
```

---

## Repository Pattern

Repository interface → domain/repositories
Implementation → infrastructure/database/repositories

Never access database directly from use case.

---

## Schema Rules

Separate schemas:

UserCreate → request
UserResponse → response

Never return ORM models.

---

## FastAPI Rules

Routes must:

* Be thin controllers
* Instantiate use case
* Inject DB session
* Return response schema

---

## Code Quality

Always:

* Type hint everything
* Use dependency injection
* Keep functions small
* Prefer composition over inheritance
* Follow SOLID principles
* When printing, use logging instead of print statements
* When querying the database, use ORM models, not raw SQL queries
* When querying the database, use the repository pattern, not direct access to the database session

Avoid:

* fat routes
* global database access
* mixing ORM and domain models

---

## When creating a new module

Generate ALL required layers:

1. domain entity
2. repository interface
3. SQLAlchemy model
4. repository implementation
5. use case(s)
6. schemas
7. API endpoint
8. router registration

Ensure imports follow architecture direction.

---

End of instructions.

