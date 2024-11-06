from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .models import Calculation

# Function to create a new calculation record
async def create_calculation(session: AsyncSession, operation: str, x: float, y: float, result: float):
    calculation = Calculation(operation=operation, x=x, y=y, result=result)
    session.add(calculation)
    await session.commit()
    await session.refresh(calculation)
    return calculation

# Function to retrieve all calculation records
async def get_all_calculations(session: AsyncSession):
    result = await session.execute(select(Calculation))
    return result.scalars().all()
