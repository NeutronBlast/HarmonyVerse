"""SQLite database connection

This scripts allows the database connection to the SQLite database chinook.db that contains all the information
stored in the music site

This script requires that SQLalchemy is installed within the Python environment you're running this script in
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///chinook.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
