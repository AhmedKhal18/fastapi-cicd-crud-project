import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load .env variables from root
load_dotenv()

# Get DB URL from environment
DATABASE_URL = os.getenv("DB_URL")
print("DB URL:", DATABASE_URL)  # Optional: remove after debugging

# Create SQLAlchemy async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create session
SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Base model
Base = declarative_base()
