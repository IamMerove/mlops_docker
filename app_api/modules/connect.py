import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# LOGIQUE : Si DATABASE_URL n'est pas définie (en local), on utilise SQLite

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./local_test.db")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def init_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
