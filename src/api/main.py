from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from api.database import get_db  
from schemas import SurveyInput
from api.crud import submit_survey

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use your domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/submit")
def submit_survey(data: SurveyInput, db: Session = Depends(get_db)):
    user_id = submit_survey(db, data)
    return {"status": "success", "user_id": str(user_id)}