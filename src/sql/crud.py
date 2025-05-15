from uuid import uuid4
from sqlalchemy.orm import Session
from src.sql.tables import UserID, Q1, Q2, Q3, Q4, Q5, Q6


def submit_survey(db: Session, survey_data: dict):
    new_user_id = uuid4()
    db.add(UserID(id=new_user_id))

    for ans_id in survey_data["q1"]:
        db.add(Q1(user_id=new_user_id, answer_id=ans_id))
    for ans_id in survey_data["q2"]:
        db.add(Q2(user_id=new_user_id, answer_id=ans_id))
    for ans_id in survey_data["q3"]:
        db.add(Q3(user_id=new_user_id, answer_id=ans_id))
    for ans_id in survey_data["q4"]:
        db.add(Q4(user_id=new_user_id, answer_id=ans_id))
    for ans_id in survey_data["q5"]:
        db.add(Q5(user_id=new_user_id, answer_id=ans_id))

    db.add(
        Q6(
            user_id=new_user_id,
            contact_info=survey_data.get("q6"),
            declined=survey_data.get("declined", False),
        )
    )

    db.commit()
    return new_user_id
