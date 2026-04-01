from fastapi import APIRouter
from ..utils.security import create_token

router = APIRouter()

@router.post("/login")
def login():
    return {"access_token": create_token({"user": "admin", "role": "admin"})}
