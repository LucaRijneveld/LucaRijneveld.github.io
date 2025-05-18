from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

# Replace with your SQLite path or another DB connection string
SQLALCHEMY_DATABASE_URL = "sqlite:///./portfolio.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency to get a DB session
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
