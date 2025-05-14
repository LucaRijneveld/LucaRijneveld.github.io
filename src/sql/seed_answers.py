from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from tables import AnswersQ1, AnswersQ2, AnswersQ3, AnswersQ4, AnswersQ5, Base

# Set up your engine (update if using PostgreSQL later)
engine = create_engine("sqlite:///src/sql/portfolio.db", echo=True)
Base.metadata.create_all(engine)

# Answers to populate
q1_answers = ["LinkedIn", "GitHub", "Google", "University", "Friend", "Other"]
q2_answers = ["Tech", "Gaming", "Academia", "Business", "Other"]
q3_answers = ["Data Science", "AI", "AI & Games", "Business Analytics"]
q4_answers = [
    "Recruiter",
    "Student",
    "Lecturer",
    "Researcher",
    "Developer",
    "Founder",
    "Other",
]
q5_answers = [
    "Minecraft",
    "League of Legends",
    "World of Warcraft",
    "Valorant",
    "Elden Ring",
    "Dungeons & Dragons",
    "Apex Legends",
    "None",
]

with Session(engine) as session:
    for ans in q1_answers:
        session.add(AnswersQ1(answer=ans))
    for ans in q2_answers:
        session.add(AnswersQ2(answer=ans))
    for ans in q3_answers:
        session.add(AnswersQ3(answer=ans))
    for ans in q4_answers:
        session.add(AnswersQ4(answer=ans))
    for ans in q5_answers:
        session.add(AnswersQ5(answer=ans))

    session.commit()
    print("Answer tables populated.")
