from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# PostgreSQL database URL
database_url = 'postgresql://username:password@host/database_name'

engine = create_engine("postgresql://user:password@localhost:5432/portfolio")
Base.metadata.create_all(engine)
