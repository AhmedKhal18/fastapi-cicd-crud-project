from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import SessionLocal, engine, Base
from app import crud
from fastapi import HTTPException

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


@app.put("/users/{user_id}")
async def update_user(
    user_id: int, name: str, email: str, db: AsyncSession = Depends(get_db)
):
    user = await crud.update_user(db, user_id, name, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.delete("/users/{user_id}")
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await crud.delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": f"User {user_id} deleted successfully"}
