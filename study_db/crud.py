from sqlalchemy import create_engine
from config import DATABASE_URI
from models import Base, Book, Genre
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

import yaml

engine = create_engine(DATABASE_URI, echo=False)
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


# load_yaml(Genre, "genres")
# print(*s.query(Genre).all(), sep="\n")
def load_yaml(ModelName, table_name: str):
    with session_scope() as s:
        for data in yaml.load_all(open(f"{table_name}.yaml"), Loader=yaml.SafeLoader):
            new_data = ModelName(**data)
            s.add(new_data)


if __name__ == "__main__":
    with session_scope() as s:
        print(*s.query(Genre).all(), sep="\n")
        print(*s.query(Book).all(), sep="\n")
