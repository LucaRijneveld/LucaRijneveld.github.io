from fastapi import FastAPI
from src.sql import crud

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/submit")
def submit_survey(data: SurveyInput, db: Session = Depends(get_db)):
    user_id = crud.submit_survey(db, data.dict())
    return {"status": "success", "user_id": str(user_id)}
