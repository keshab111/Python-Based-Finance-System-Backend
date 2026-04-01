from sqlalchemy.orm import Session
from . import models, schemas

def create_transaction(db: Session, txn: schemas.TransactionCreate):
    db_txn = models.Transaction(**txn.dict())
    db.add(db_txn)
    db.commit()
    db.refresh(db_txn)
    return db_txn

def get_transactions(db: Session):
    return db.query(models.Transaction).all()
