# calculator_app/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import async_session, init_db
from database.crud import create_calculation
from database.models import Calculation
from typing import List
from database.crud import get_all_calculations
from database.schemas import CalculationSchema


app = FastAPI()

# Dependency to provide an async database session
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

# Initialize the database
@app.on_event("startup")
async def startup():
    await init_db()

# Calculator operations
@app.get("/add")
async def add(x: float, y: float, session: AsyncSession = Depends(get_session)):
    result = x + y
    await create_calculation(session, "addition", x, y, result)
    return {"operation": "addition", "x": x, "y": y, "result": result}

@app.get("/subtract")
async def subtract(x: float, y: float, session: AsyncSession = Depends(get_session)):
    result = x - y
    await create_calculation(session, "subtraction", x, y, result)
    return {"operation": "subtraction", "x": x, "y": y, "result": result}

@app.get("/multiply")
async def multiply(x: float, y: float, session: AsyncSession = Depends(get_session)):
    result = x * y
    await create_calculation(session, "multiplication", x, y, result)
    return {"operation": "multiplication", "x": x, "y": y, "result": result}

@app.get("/divide")
async def divide(x: float, y: float, session: AsyncSession = Depends(get_session)):
    if y == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    result = x / y
    await create_calculation(session, "division", x, y, result)
    return {"operation": "division", "x": x, "y": y, "result": result}

# Define the endpoint to retrieve all calculations
@app.get("/calculations", response_model=List[CalculationSchema])
async def read_calculations(session: AsyncSession = Depends(get_session)):
    calculations = await get_all_calculations(session)
    return calculations
