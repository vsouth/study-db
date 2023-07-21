import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from models import Base, Book

from datetime import datetime


load_dotenv()
DATABASE_URI = os.getenv("DATABASE_URI")

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)


def create_database():
    Base.metadata.create_all(engine)


def drop_database():
    Base.metadata.drop_all(engine)


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def main():
    book = Book(
        title="Deep Learning",
        author="Ian Goodfellow",
        pages=775,
        published=datetime(2016, 11, 18),
    )

    recreate_database()
    s = Session()
    s.add(book)
    s.commit()
    print(s.query(Book).first())
    s.close()
