Fastapi Manager

A simple Task Manager REST API built. It allows users to securely register, log in using JWT authentication, and manage their own tasks. Each user can create, view, update, and delete only their own tasks.
This application supports


## Features

- User Registration
- User Login with JWT Authentication
- Password Hashing using bcrypt
- Protected API Endpoints
- User-specific Task Management
- Create, Read, Update, and Delete (CRUD) Operations
- SQLite Database Integration
- SQLAlchemy ORM
- Pydantic Data Validation
- Interactive Swagger API Documentation

## Technologies Used

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- Passlib (bcrypt)
- Python-JOSE (JWT)
- Uvicorn

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/fastapi-task-manager.git
cd fastapi-task-manager
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
uvicorn app.main:app --reload
```

4. Open Swagger UI:
```
http://127.0.0.1:8000/docs
```

## API Endpoints

### Authentication

- POST `/auth/signup` – Register a new user
- POST `/auth/login` – Login and receive JWT token
- GET `/auth/me` – Get logged-in user details

### Tasks

- POST `/tasks` – Create a new task
- GET `/tasks` – View all tasks of the logged-in user
- GET `/tasks/{id}` – View a specific task
- PUT `/tasks/{id}` – Update a task
- DELETE `/tasks/{id}` – Delete a task

## Project Structure

```
fastapi-task-manager/
│
├── app/
│   ├── auth.py
│   ├── config.py
│   ├── crud.py
│   ├── database.py
│   ├── dependencies.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── __init__.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── task_manager.db
```

## Future Enhancements

- Refresh Token Support
- Forgot Password API
- Email Verification
- Role-Based Access Control (Admin/User)
- Docker Deployment
- Pagination and Task Search

## Author
Tekam Sridhar

**Sridhar Tekam**
