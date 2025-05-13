# src/sql/db_init.py
from sqlalchemy import create_engine
from models import Base

engine = create_engine("postgresql://user:password@localhost:5432/portfolio")
Base.metadata.create_all(engine)
