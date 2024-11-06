# calculator_app/database/database.py
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from .models import Base
from config import DATABASE_URL

# Create an async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Async sessionmaker for creating database sessions
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

# Create the database tables
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
