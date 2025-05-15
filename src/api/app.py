from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from src.sql import crud
from src.sql.database import get_db
from src.api.schemas import SurveyInput  # your Pydantic model

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],  # or restrict to ["http://localhost:3000"] or your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/submit")
async def submit_survey(data: SurveyInput, db: Session = Depends(get_db)):
    print("Received data:", data)
    user_id = crud.submit_survey(db, data.dict())
    return {"status": "success", "user_id": str(user_id)}
