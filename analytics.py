from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models

router = APIRouter(prefix="/analytics")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/summary")
def summary(db: Session = Depends(get_db)):
    txns = db.query(models.Transaction).all()

    income = sum(t.amount for t in txns if t.type == "income")
    expense = sum(t.amount for t in txns if t.type == "expense")

    return {
        "total_income": income,
        "total_expense": expense,
        "balance": income - expense
    }
