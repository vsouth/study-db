from datetime import datetime

from sqlalchemy import create_engine
from config import DATABASE_URI
from models import Base, Book
from sqlalchemy.orm import sessionmaker

from sqlalchemy import and_, or_


engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)


def create_database():
    Base.metadata.create_all(engine)


def drop_database():
    Base.metadata.drop_all(engine)


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    s = Session()
    # books either less than 500 pages or greater than 750 pages long
    # books published between 2013 and 2017
    # ordered by the number of pages
    # limit it to one result

    r = (
        s.query(Book)
        .filter(
            and_(
                or_(Book.pages < 500, Book.pages > 750),
                Book.published.between(datetime(2013, 1, 1), datetime(2017, 1, 1)),
            )
        )
        .order_by(Book.pages.desc())
        .limit(1)
        .first()
    )

    print("FINAL:\n", r, "\n")

    s.close()
