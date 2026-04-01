from fastapi import FastAPI
from .database import engine
from . import models
from .routes import transaction, analytics, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Finance Tracker API")

app.include_router(transaction.router)
app.include_router(analytics.router)
app.include_router(auth.router)

@app.get("/")
def home():
    return {"message": "API Running 🚀"}
