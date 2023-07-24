from datetime import datetime

from sqlalchemy import create_engine
from config import DATABASE_URI
from models import Base, Book
from sqlalchemy.orm import sessionmaker

from sqlalchemy import and_, or_

from contextlib import contextmanager

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)


def create_database():
    Base.metadata.create_all(engine)


def drop_database():
    Base.metadata.drop_all(engine)


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


if __name__ == "__main__":
    with session_scope() as s:
        print(*s.query(Book).all(), sep="\n")
