from fastapi import APIRouter, HTTPException
from decimal import Decimal, InvalidOperation
from models import DivisionResult

router = APIRouter(tags=['Number_operations'])

@router.get("/div", response_model=DivisionResult)
def divide(a: int, b: int):
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    
    try:
        result = Decimal(a) / Decimal(b)
    except InvalidOperation as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return DivisionResult(a=a, b=b, result=result)
