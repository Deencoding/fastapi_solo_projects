# calculator_app/schemas.py
from pydantic import BaseModel

# Define the Pydantic schema for the Calculation data
class CalculationSchema(BaseModel):
    id: int
    operation: str
    x: float
    y: float
    result: float

    class Config:
        orm_mode = True
