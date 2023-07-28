import sys, os

sys.path.insert(0, os.path.dirname(__file__))

from crud import session_scope
from models import Book, Genre


def add_book_by_hand():
    with session_scope() as s:
        title = input("Book title: ")
        author = input("Book author: ")
        book = Book(title=title, author=author)
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


if __name__ == "__main__":
    with session_scope() as s:
        pass
