# 🚀 FastAPI CI/CD CRUD Project

A full-stack backend project demonstrating **FastAPI CRUD operations**, containerized using **Docker** and connected to a **PostgreSQL** database. Linting and type-checking are enforced via `black`, `flake8`, and `mypy` using `pre-commit` hooks.

---

## 📌 Phase 1 Features

✅ **FastAPI** backend with full CRUD (Create, Read, Update, Delete) operations  
✅ **Docker** containerization  
✅ **PostgreSQL** integration via Docker Compose  
✅ **Environment configuration** using `.env`  
✅ **Pre-commit hooks** with `black`, `flake8`, and `mypy`  
✅ Swagger UI documentation at `/docs`

---

## 📁 Project Structure
. ├── app │ ├── crud.py │ ├── database.py │ ├── main.py │ ├── models.py │ └── tests/ ├── Dockerfile ├── docker-compose.yml ├── requirements.txt ├── .env └── .pre-commit-config.yaml

---

## 🐳 How to Run

### 1. Clone the repo
```bash
git clone https://github.com/AhmedKhal18/fastapi-cicd-crud-project.git
cd fastapi-cicd-crud-project
```
2. Create .env
```bash
DB_URL=postgresql+asyncpg://postgres:devpassword@postgres-devops:5432/devops_db
```
3. Run with Docker Compose
```bash
docker-compose up --build
```
App will be available at: http://localhost:8000/docs
✅ Endpoints
GET	/	Health check
GET	/users	Get all users
POST	/users	Add a new user
PUT	/users/{user_id}	Update a user
DELETE	/users/{user_id}	Delete a user

🧹 Linting & Type Checking
Run the following locally before pushing:
```bash
pre-commit run --all-files
```
Ensures formatting with black, linting with flake8, and static type checks via mypy.
📦 Technologies Used
FastAPI
SQLAlchemy (Async)
PostgreSQL
Docker & Docker Compose
Pre-commit Hooks (black, flake8, mypy)

📌 Phase 2 (Coming Up)
Next steps will include:

CI/CD Pipeline with GitHub Actions

Automated testing

Multi-environment deployment

Monitoring/logging stack

Author
Ahmed Khalil
GitHub @AhmedKhal18





