import sys, os

sys.path.insert(0, os.path.dirname(__file__))

from crud import session_scope
from models import Book, Genre, Author


def add_author_by_hand():
    with session_scope() as s:
        name = input("Author name: ")
        biography = input("Author biography: ")
        author = Author(name=name, biography=biography)
        s.add(author)


def add_book_by_hand():
    with session_scope() as s:
        title = input("Book title: ")
        author_name = input("Book author: ")
        book = Book(title=title, author_name=author_name)
        s.add(book)


def add_genre_by_hand():
    with session_scope() as s:
        name = input("Genre name: ")
        description = input("Genre description: ")
        genre = Genre(name=name, description=description)


def add_book_genres_by_hand():
    with session_scope() as s:
        all_genres = s.query(Genre).all()
        print(*all_genres, sep="\n")
        books = s.query(Book).filter(Book.genres == None).all()
        for book in books:
            genres = [
                all_genres[int(i) - 1]
                for i in input(f"Genres of '{book.title}': ").split(" ")
            ]
            book.genres = genres
            s.add(book)


def get_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
        return instance


def give_books_author_ids():
    with session_scope() as s:
        books = s.query(Book).filter(Book.author == None).all()
        authors = s.query(Author).all()
        for book in books:
            author = get_or_create(s, Author, name=book.author_name)
            book.author_id = author.id


if __name__ == "__main__":
    give_books_author_ids()
