from uuid import uuid4, UUID
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import sqlalchemy.types as types


class Base(DeclarativeBase):
    pass


"""
Below are the tables for the portfolio questionnaire. These tables store the int that the question maps to.
"""


class UserID(Base):
    __tablename__ = "user_id"

    id: Mapped[UUID] = mapped_column(
        types.Uuid, primary_key=True, default=uuid4, index=True
    )


class Consent(Base):
    __tablename__ = "consent"

    id: Mapped[UUID] = mapped_column(
        types.Uuid, primary_key=True, default=uuid4, index=True
    )
    user_id: Mapped[UUID] = mapped_column(
        types.Uuid, ForeignKey("user_id.id"), nullable=False
    )
    consent: Mapped[bool] = mapped_column(types.Boolean, default=False)


# How did you learn about my portfolio?
class Q1(Base):
    __tablename__ = "q1"

    id: Mapped[UUID] = mapped_column(
        types.Uuid, primary_key=True, default=uuid4, index=True
    )
    user_id: Mapped[UUID] = mapped_column(
        types.Uuid, ForeignKey("user_id.id"), nullable=False
    )
    answer_id: Mapped[int] = mapped_column(
        ForeignKey("answers_q1.id"), nullable=False
    )


# What industry do you work in?
class Q2(Base):
    __tablename__ = "q2"

    id: Mapped[UUID] = mapped_column(
        types.Uuid, primary_key=True, default=uuid4, index=True
    )
    user_id: Mapped[UUID] = mapped_column(
        types.Uuid, ForeignKey("user_id.id"), nullable=False
    )
    answer_id: Mapped[int] = mapped_column(
        ForeignKey("answers_q2.id"), nullable=False
    )


# What are you looking for/ interested in?
class Q3(Base):
    __tablename__ = "q3"

    id: Mapped[UUID] = mapped_column(
        types.Uuid, primary_key=True, default=uuid4, index=True
    )
    user_id: Mapped[UUID] = mapped_column(
        types.Uuid, ForeignKey("user_id.id"), nullable=False
    )
    answer_id: Mapped[int] = mapped_column(
        ForeignKey("answers_q3.id"), nullable=False
    )


# What is your role?
class Q4(Base):
    __tablename__ = "q4"

    id: Mapped[UUID] = mapped_column(
        types.Uuid, primary_key=True, default=uuid4, index=True
    )
    user_id: Mapped[UUID] = mapped_column(
        types.Uuid, ForeignKey("user_id.id"), nullable=False
    )
    answer_id: Mapped[int] = mapped_column(
        ForeignKey("answers_q4.id"), nullable=False
    )


# What games do you play in your free time?
class Q5(Base):
    __tablename__ = "q5"

    id: Mapped[UUID] = mapped_column(
        types.Uuid, primary_key=True, default=uuid4, index=True
    )
    user_id: Mapped[UUID] = mapped_column(
        types.Uuid, ForeignKey("user_id.id"), nullable=False
    )
    answer_id: Mapped[int] = mapped_column(
        ForeignKey("answers_q5.id"), nullable=False
    )


# Contact information
class Q6(Base):
    __tablename__ = "q6"
    id: Mapped[UUID] = mapped_column(
        types.Uuid, primary_key=True, default=uuid4
    )
    user_id: Mapped[UUID] = mapped_column(
        types.Uuid, ForeignKey("user_id.id"), nullable=False
    )
    contact_info: Mapped[Optional[str]] = mapped_column(
        types.String(255), nullable=True
    )
    declined: Mapped[bool] = mapped_column(types.Boolean, default=False)


class Q7(Base):
    __tablename__ = "q7"
    id: Mapped[UUID] = mapped_column(
        types.Uuid, primary_key=True, default=uuid4
    )
    user_id: Mapped[UUID] = mapped_column(
        types.Uuid, ForeignKey("user_id.id"), nullable=False
    )
    question: Mapped[Optional[str]] = mapped_column(
        types.String(1677219), nullable=True
    )
    declined: Mapped[bool] = mapped_column(types.Boolean, default=False)


"""
Here are the tables for the answers. These tables map to the int in the previous tables. Only Q1-Q5 have answers. Q6 is stored as a string.
"""


class AnswersQ1(Base):
    __tablename__ = "answers_q1"

    id: Mapped[int] = mapped_column(
        types.Integer, primary_key=True, index=True
    )
    answer: Mapped[str] = mapped_column(types.String(255), default="")


class AnswersQ2(Base):
    __tablename__ = "answers_q2"

    id: Mapped[int] = mapped_column(
        types.Integer, primary_key=True, index=True
    )
    answer: Mapped[str] = mapped_column(types.String(255), default="")


class AnswersQ3(Base):
    __tablename__ = "answers_q3"

    id: Mapped[int] = mapped_column(
        types.Integer, primary_key=True, index=True
    )
    answer: Mapped[str] = mapped_column(types.String(255), default="")


class AnswersQ4(Base):
    __tablename__ = "answers_q4"

    id: Mapped[int] = mapped_column(
        types.Integer, primary_key=True, index=True
    )
    answer: Mapped[str] = mapped_column(types.String(255), default="")


class AnswersQ5(Base):
    __tablename__ = "answers_q5"

    id: Mapped[int] = mapped_column(
        types.Integer, primary_key=True, index=True
    )
    answer: Mapped[str] = mapped_column(types.String(255), default="")
