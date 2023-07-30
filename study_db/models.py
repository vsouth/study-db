from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Table, Column, Integer, String, Text, ForeignKey


Base = declarative_base()


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    biography = Column(Text)

    books = relationship("Book", back_populates="author")

    def __repr__(self):
        return (
            f" <Author(id={self.id}, name='{self.name}', biography='{self.biography}')>"
        )


class Genre(Base):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)

    def __str__(self):
        return f" <Genre(id={self.id}, name='{self.name}', description='{self.description}')>"

    def __repr__(self):
        return f"{self.name}"


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

    author_id = Column(Integer, ForeignKey("authors.id"))

    author = relationship("Author", back_populates="books")
    genres = relationship("Genre", secondary="book_genre")

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', author='{self.author.name}', genres={self.genres})>"


book_genre = Table(
    "book_genre",
    Base.metadata,
    Column("book_id", Integer, ForeignKey("books.id"), primary_key=True),
    Column("genre_id", Integer, ForeignKey("genres.id"), primary_key=True),
)
