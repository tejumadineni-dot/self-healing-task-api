#  Task Management API (Self-Healing System)

##  Project Overview
This project is a Task Management REST API built using FastAPI and SQLAlchemy.

It is designed with a focus on production-level backend concepts such as modular architecture, self-healing retry mechanism, structured logging, and scalable API design.

The system allows users to perform CRUD operations on tasks while ensuring stability even during failures.

---

##  Key Highlights
- Production-style backend architecture
- Self-healing retry mechanism for database failures
- Structured logging with unique request ID tracking
- Scalable API design using pagination
- Clean modular code structure

---

##  Tech Stack
- Python
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn
- SQLite
- Logging module

---

##  How It Works
Client → FastAPI → Routes → Database → Logging System  
Each request is tracked, processed, and logged with a unique request ID. Retry logic handles database failures automatically.

---

##  System Design
Client → FastAPI → Routes → Database  
                     ↓  
                  Logging System  

---

##  Architecture
- Routes layer (API endpoints)
- Schemas layer (validation)
- Database layer (models & connection)
- Logging module (observability)

---

##  Error Handling Strategy
- Retry mechanism for database operations
- Centralized exception handling
- Proper logging for debugging and monitoring

---

##  What I Learned
- Designing modular backend architecture
- Implementing retry mechanism for fault tolerance
- Writing scalable API structure
- Using structured logging for production systems

---

##  Project Structure
app/
├── main.py
├── routes.py
├── schemas.py
├── logger.py
├── config.py
├── database/
│   ├── db.py
│   ├── models.py
│   ├── deps.py

---

##  Setup Instructions

1. Create virtual environment  
python -m venv venv  

2. Activate environment  
venv\Scripts\activate   (Windows)  
source venv/bin/activate   (Mac/Linux)  

3. Install dependencies  
pip install fastapi uvicorn sqlalchemy pydantic pydantic-settings  

4. Run application  
uvicorn app.main:app --reload  

---

##  API Endpoints

- GET /health → Health check  
- POST /tasks → Create task  
- GET /tasks → Get all tasks (pagination)  
- PUT /tasks/{id} → Update task  
- DELETE /tasks/{id} → Delete task  

---

##  Testing
- Swagger UI → /docs  
- Manual API testing (POST/GET/PUT/DELETE)

---

##  Future Improvements
- JWT Authentication
- PostgreSQL integration
- Docker containerization
- CI/CD pipeline
- Cloud deployment (AWS / Render)
- AI-based task prioritization

---

##  Project Status
✔ Completed  
✔ Tested  
✔ Ready for production-style deployment  

---

##  Conclusion
This project demonstrates a production-ready backend system built using FastAPI.

It includes real-world engineering practices like fault tolerance, structured logging, modular architecture, and scalable API design.

This is not just a CRUD project — it simulates how real backend systems are built in production environments.