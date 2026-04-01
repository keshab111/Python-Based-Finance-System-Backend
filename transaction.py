from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models, crud, schemas

router = APIRouter(prefix="/transactions")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create(txn: schemas.TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db, txn)

@router.get("/")
def get_all(type: str = Query(None), category: str = Query(None), page: int = 1, limit: int = 5, db: Session = Depends(get_db)):
    query = db.query(models.Transaction)

    if type:
        query = query.filter(models.Transaction.type == type)

    if category:
        query = query.filter(models.Transaction.category == category)

    total = query.count()
    data = query.offset((page - 1) * limit).limit(limit).all()

    return {"total": total, "data": data}
