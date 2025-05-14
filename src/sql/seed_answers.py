from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from tables import AnswersQ1, AnswersQ2, AnswersQ3, AnswersQ4, AnswersQ5, Base

# Set up your engine (update if using PostgreSQL later)
engine = create_engine("sqlite:///src/sql/portfolio.db", echo=True)
Base.metadata.create_all(engine)

# Answers to populate
q5_answers = [
    "Other"
]

with Session(engine) as session:
    for ans in q5_answers:
        session.add(AnswersQ5(answer=ans))

    session.commit()
    print("Answer tables populated.")
