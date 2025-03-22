
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import SessionLocal, engine, Base
from app import crud

app = FastAPI()

# Create tables at startup
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Dependency
async def get_db():
    async with SessionLocal() as session:
        yield session

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
async def read_users(db: AsyncSession = Depends(get_db)):
    return await crud.get_users(db)

@app.post("/users")
async def add_user(name: str, email: str, db: AsyncSession = Depends(get_db)):
    return await crud.create_user(db, name, email)
