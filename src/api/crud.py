from uuid import uuid4
from tables import UserID, Q1, Q2, Q3, Q4, Q5, Q6
from sqlalchemy.orm import Session

def submit_survey(db: Session, data):
    user_id = uuid4()
    db.add(UserID(id=user_id))

    for ans_id in data.q1:
        db.add(Q1(user_id=user_id, answer_id=ans_id))
    for ans_id in data.q2:
        db.add(Q2(user_id=user_id, answer_id=ans_id))
    for ans_id in data.q3:
        db.add(Q3(user_id=user_id, answer_id=ans_id))
    for ans_id in data.q4:
        db.add(Q4(user_id=user_id, answer_id=ans_id))
    for ans_id in data.q5:
        db.add(Q5(user_id=user_id, answer_id=ans_id))

    db.add(Q6(
        user_id=user_id,
        contact_info=data.q6 if not data.declined else None,
        declined=data.declined
    ))

    db.commit()
    return user_id
