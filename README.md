Task Management API (Self-Healing System)

 Project Overview

This project is a Task Management API built using FastAPI and SQLAlchemy with a focus on self-healing and robust error handling.

It allows users to perform CRUD operations on tasks while ensuring the system remains stable even when errors occur.

---

 Tech Stack

- Python 
- FastAPI 
- SQLAlchemy 
- Pydantic 
- Uvicorn 
- Logging module 

---

 Key Features

-  CRUD Operations (Create, Read, Update, Delete)
-  Self-healing error handling (no crash system)
-  Structured logging instead of print statements
-  Input validation using Pydantic
-  Clean modular architecture

---

 Project Structure

app/
├── main.py        # Entry point
├── routes.py      # API routes
├── schemas.py     # Validation models
├── database/      # DB models & connection
├── logger.py      # Logging system

---

 API Endpoints

- POST /tasks → Create task
- GET /tasks → Get all tasks
- PUT /tasks/{id} → Update task
- DELETE /tasks/{id} → Delete task

---

 How to Run

# 1. Create virtual environment
python -m venv venv

# 2. Activate environment
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run server
uvicorn app.main:app --reload

---

 API Docs

After running the server, open:
 http://127.0.0.1:8000/docs

---

 Future Improvements

-  AI-based task prioritization
-  Notifications system
-  Task analytics dashboard
-  Authentication & Authorization

---

 Conclusion

This project demonstrates building production-ready APIs with proper structure, validation, and error handling, making the system reliable and scalable.