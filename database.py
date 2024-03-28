from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# echo = True
engine = create_engine("sqlite:///library.db")
session = Session(bind=engine)
