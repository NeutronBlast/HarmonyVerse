# SQLite database connection
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///chinook.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)