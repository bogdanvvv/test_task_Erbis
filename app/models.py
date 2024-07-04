from pydantic import BaseModel, Field
from decimal import Decimal

class DivisionResult(BaseModel):
    a: int
    b: int
    result: Decimal = Field(..., description="The result of the division")
