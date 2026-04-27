#  Task Management API (Self-Healing  System)

A production-style backend API built using FastAPI + SQLAlchemy.  
This project focuses on modular architecture, logging, retry mechanism, and unit testing.

---

#  System Architecture

Client (Postman / Frontend)  
↓  
FastAPI (main.py)  
↓  
Routes Layer  
↓  
Service Layer  
↓  
Database Layer   
↓  
Logging + Retry System  
↓  
Response

---

# 📁 Project Structure

task-api/
│
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── schemas.py
│   ├── logger.py
│   ├── config.py
│   │
│   ├── services/
│   │   └── task_service.py
│   │
│   ├── database/
│       ├── db.py
│       ├── models.py
│       └── deps.py
│
├── test_task.py
├── requirements.txt
├── technical Architecture.txt

---

#  Tech Stack

Python  
FastAPI  
SQLAlchemy  
Pydantic  
Uvicorn  
Pytest

---

#  Features

- CRUD operations for tasks  
- Service layer architecture  
- Structured logging with request ID  
- Retry mechanism for DB failures (self-healing)  
- Pagination support  
- Input validation using Pydantic  
- Unit testing using pytest  

---

#  Request Flow

                ┌────────────────────────────┐
                │   Client (Postman / UI)    │
                └─────────────┬──────────────┘
                              │
                              ▼
                ┌────────────────────────────┐
                │     FastAPI (main.py)      │
                │  Entry Point / App Layer   │
                └─────────────┬──────────────┘
                              │
                              ▼
                ┌────────────────────────────┐
                │      Routes Layer          │
                │  (API Endpoints Handler)   │
                └─────────────┬──────────────┘
                              │
                              ▼
                ┌────────────────────────────┐
                │     Service Layer          │
                │ (Business Logic Layer)     │
                └─────────────┬──────────────┘
                              │
              ┌───────────────┴───────────────┐
              ▼                               ▼
   ┌────────────────────┐        ┌────────────────────┐
   │  Logging System     │        │ Retry Mechanism    │
   │ (Request Tracking)  │        │ (Self-Healing DB)  │
   └─────────┬──────────┘        └─────────┬──────────┘
             │                              │
             └──────────────┬──────────────┘
                            ▼
                ┌────────────────────────────┐
                │     Database Layer         │
                │ (SQLAlchemy + SQLite)      │
                └─────────────┬──────────────┘
                              │
                              ▼
                ┌────────────────────────────┐
                │        Response            │
                │   JSON Output to Client    │
                └────────────────────────────┘
---

#  Error Handling Strategy

- Global exception handling  
- Retry mechanism for database operations  
- Structured logging for debugging  

---

#  Testing

Run tests:

pytest

Expected output:

1 passed

---

#  Run Project

uvicorn app.main:app --reload

---

#  API Endpoints

GET /health → Health check  
POST /tasks → Create task  
GET /tasks → Get all tasks  
PUT /tasks/{id} → Update task  
DELETE /tasks/{id} → Delete task  

---

#  What I Learned

- Backend architecture design (Service Layer)  
- Logging system implementation  
- Retry mechanism for fault tolerance  
- Unit testing with pytest  
- Clean modular coding practices  

---

#  Future Improvements

- JWT Authentication  
- PostgreSQL integration  
- Docker containerization  
- CI/CD pipeline  
- Cloud deployment  

---

#  Project Status

Completed  
Tested 
Production-style backend   
