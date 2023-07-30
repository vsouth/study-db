from sqlalchemy.orm import Session

from models import Book, Genre, Author


import yaml

from database import SessionLocal_scope, SessionLocal


# load_yaml(Genre, "genres")
# print(*s.query(Genre).all(), sep="\n")
def load_yaml(ModelName, table_name: str):
    with SessionLocal_scope() as s:
        for data in yaml.load_all(open(f"{table_name}.yaml"), Loader=yaml.SafeLoader):
            new_data = ModelName(**data)
            s.add(new_data)


def get_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
        return instance


def get_all_genres():
    with SessionLocal_scope() as s:
        return s.query(Genre).all()


def get_all_books():
    with SessionLocal_scope() as s:
        return s.query(Book).all()


def get_all_authors():
    with SessionLocal_scope() as s:
        return s.query(Author).all()


# C R E A T E


def create_author(db: Session, name: str, biography: str):
    db_author = Author(name=name, biography=biography)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def create_book(db: Session, title: str, author_id: int):
    db_book = Book(title=title, author_id=author_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def create_genre(db: Session, name: str, description: str):
    db_genre = Genre(name=name, description=description)
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)
    return db_genre


# R E A D


def get_author(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()


def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def get_genre(db: Session, genre_id: int):
    return db.query(Genre).filter(Genre.id == genre_id).first()


if __name__ == "__main__":
    pass
