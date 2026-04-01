from pydantic import BaseModel

class TransactionCreate(BaseModel):
    amount: float
    type: str
    category: str
    date: str
    note: str

class TransactionResponse(TransactionCreate):
    id: int

    class Config:
        orm_mode = True
