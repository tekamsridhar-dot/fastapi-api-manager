Fastapi Manager

A simple Task Manager REST API built using 
 1.Python
2.FastAPI, 
3.SQLite
4.SQLAlchemy
5.Pydantic

This application supports
 CRUD operations to 
 1.create 
 2.view 
 3.update  
 4.delete tasks.

 Setup

bash
pip install -r requirements.txt
uvicorn app.main:app --reload

Open Swagger UI:

http://127.0.0.1:8000/docs

API Endpoints

- **POST** `/tasks` – Add a task
- **GET** `/tasks` – View all tasks
- **PUT** `/tasks/{id}` – Update a task
- **DELETE** `/tasks/{id}` – Delete a task
