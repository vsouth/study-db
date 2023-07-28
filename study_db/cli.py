from crud import session_scope
from models import Book, Genre


def add_genres_by_hand():
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
        book = s.query(Book).filter(Book.title == "Mother").first()
        book.author = "J. Mama"
