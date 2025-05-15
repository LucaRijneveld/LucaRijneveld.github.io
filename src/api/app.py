from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.sql import crud
from src.sql.database import get_db
from src.api.schemas import SurveyInput  # your Pydantic model

app = FastAPI()


@app.post("/submit")
def submit_survey(data: SurveyInput, db: Session = Depends(get_db)):
    user_id = crud.submit_survey(db, data.dict())
    return {"status": "success", "user_id": str(user_id)}
