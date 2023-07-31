from sqlalchemy.orm import joinedload, load_only

import crud
from models import Book, Genre, Author, book_genre


# CREATE


def add_author():
    with crud.session_scope() as s:
        name = input("Author name: ")
        biography = input("Author biography: ")
        crud.create_author(s, name=name, biography=biography)


def add_book():
    with crud.session_scope() as s:
        title = input("Book title: ")
        author_name = input("Book author name: ")

        # get or create author
        response = (
            s.query(Author)
            .options(
                load_only(Author.id, Author.name),
                joinedload(Author.books).load_only(Book.title),
            )
            .filter(Author.name == author_name)
        ).all()

        for r in response:
            print(
                f"Author(id={r.id}, name={r.name}, books={', '.join([book.title for book in r.books])})"
            )

        author_id = None
        if response:
            for r in response:
                print(f"They wrote {', '.join([book.title for book in r.books])}.")
                if input("T/F or Y/N: ").upper() in ("Y", "T"):
                    author_id = r.id
                    break
        if author_id == None:
            author_biography = input("Author biography: ")
            author_id = crud.create_author(
                s, name=author_name, biography=author_biography
            ).id

        # create book genres
        all_genres = s.query(Genre).all()
        print([f"{genre.id}  {genre.name}" for genre in all_genres], sep="\n")
        user_response = input("Book genres (separate by space): ")
        if user_response != "":
            genres = [all_genres[int(i) - 1] for i in user_response.split(" ")]
        else:
            genres = None
        crud.create_book(s, title=title, author_id=author_id, genres=genres)


def add_genre():
    with crud.session_scope() as s:
        name = input("Genre name: ")
        description = input("Genre description: ")
        crud.create_genre(s, name=name, description=description)


# UPDATE


def add_book_genres_by_hand():
    with crud.session_scope() as s:
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


# READ


def get_all_authors():
    with crud.session_scope() as s:
        response = (
            s.query(Author)
            .options(joinedload(Author.books).load_only(Book.title))
            .all()
        )
        for r in response:
            print(
                f"Author(id={r.id}, name={r.name}, biography={r.biography}, books={[book.title for book in r.books]})"
            )


def get_all_books():
    with crud.session_scope() as s:
        response = (
            s.query(Book)
            .options(
                joinedload(Book.author).load_only(Author.name),
                joinedload(Book.genres).load_only(Genre.name),
            )
            .all()
        )
        for r in response:
            print(
                f"Book(id={r.id}, title={r.title}, author={r.author.name}, genres={[genre.name for genre in r.genres]})"
            )


def get_all_genres():
    with crud.session_scope() as s:
        response = s.query(Genre).all()
        for r in response:
            print(f"Genre(id={r.id}, name={r.name}, description={r.description})")


def get_all_book_genre():
    with crud.session_scope() as s:
        print(*s.query(book_genre).all(), sep="\n")
