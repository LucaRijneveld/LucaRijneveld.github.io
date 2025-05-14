from sqlalchemy import create_engine
from tables import Base

engine = create_engine("sqlite:///src/sql/portfolio.db")
Base.metadata.create_all(engine)
