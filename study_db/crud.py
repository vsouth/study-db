from sqlalchemy.orm import Session

from models import Book, Genre, Author, book_genre


import yaml

from database import session_scope, Session


# load_yaml(Genre, "genres")
# print(*s.query(Genre).all(), sep="\n")
def load_yaml(ModelName, table_name: str):
    with session_scope() as s:
        for data in yaml.load_all(open(f"{table_name}.yaml"), Loader=yaml.SafeLoader):
            new_data = ModelName(**data)
            s.add(new_data)


# C R E A T E


def create_author(db: Session, name: str, biography: str = ""):
    db_author = Author(name=name, biography=biography)
    db.add(db_author)
    db.flush()
    db.refresh(db_author)
    return db_author


def create_book(db: Session, title: str, author_id: int, genres: list[Genre] = None):
    db_book = Book(title=title, author_id=author_id, genres=genres)
    db.add(db_book)
    db.flush()
    db.refresh(db_book)
    return db_book


def create_genre(db: Session, name: str, description: str = ""):
    db_genre = Genre(name=name, description=description)
    db.add(db_genre)
    db.flush()
    db.refresh(db_genre)
    return db_genre


def create_book_genre(db: Session, book_id: int, genre_id: int):
    # db_book_genre = book_genre(book_id=book_id, genre_id=genre_id)
    # db.add(db_genre)
    # db.commit()
    # db.refresh(db_genre)
    # return db_genre
    pass


# R E A D


def get_author(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()


def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def get_genre(db: Session, genre_id: int):
    return db.query(Genre).filter(Genre.id == genre_id).first()


# U P D A T E


def update_author():
    pass


def update_book():
    pass


def update_genre():
    pass


# D E L E T E
