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

```bash
fastapi-cicd-crud-project/
├── .github/workflows/ci.yml         # CI pipeline (coming soon in Phase 2)
├── app/
│   ├── __init__.py
│   ├── crud.py                      # CRUD operations
│   ├── database.py                  # DB connection and session
│   ├── main.py                      # FastAPI app startup
│   ├── models.py                    # SQLAlchemy models
│   └── tests/
│       └── test_main.py            # Unit tests
├── .env                             # DB config (excluded via .gitignore)
├── .gitignore
├── .pre-commit-config.yaml          # Linting and type-check setup
├── Dockerfile                       # FastAPI app container
├── docker-compose.yml              # App + PostgreSQL orchestration
├── requirements.txt
└── README.md
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

🧹 Linting & Type Checking
Run the following locally before pushing:
```bash
pre-commit run --all-files
```
📸 Screenshots
![image](https://github.com/user-attachments/assets/6d0711d5-6ab7-40f6-9fe4-d7c0839c36a9)

![image](https://github.com/user-attachments/assets/f054545b-0956-43fa-978d-b21c19550bc5)

![image](https://github.com/user-attachments/assets/905f3ad9-7d0d-4bfb-907c-11eb51e51dcd)

![image](https://github.com/user-attachments/assets/dc476a78-1e12-4d51-a691-e726cc029aa5)

![image](https://github.com/user-attachments/assets/47bee20f-479f-4f69-9935-b8e047dbe7dc)

![image](https://github.com/user-attachments/assets/8c81d2ed-d29c-4289-b577-39f8cd821a08)

Ensures formatting with black, linting with flake8, and static type checks via mypy.
## 📦 Technologies Used
- FastAPI
- SQLAlchemy (Async)
- PostgreSQL
- Docker & Docker Compose
- Pre-commit Hooks (black, flake8, mypy)

## 📌 Phase 2 (Coming Up)
Next steps will include:

CI/CD Pipeline with GitHub Actions

Automated testing

Multi-environment deployment

Monitoring/logging stack

## Author
Ahmed Khalil
GitHub @AhmedKhal18





