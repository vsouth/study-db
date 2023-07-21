# TO DO
## thoughts

- should have added .gitignore for config.py (https://12factor.net/ru/config)
- decided to go with python-dotenv and .env file
- https://habr.com/ru/companies/ruvds/articles/521602/ - read later
- do it when black is doing bad job:
```
# fmt: off 
code
# fmt: on
```
- https://habr.com/ru/articles/470285/


## checklist
- [x] git + poetry (for env)
as i recall:
```
poetry new study-db
git init
git add .
git commit -m "Started" # or smth like that
# stuff on github website
git remote add origin git@github.com:vsouth/study-db.git
git push -u origin main
poetry add <smth>
poetry shell
# ctrl+shift+p > python: select interpreter > choose the poetry env one
```


- [x] create a db


- [x] write a model for a table
```
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()

class Table(Base):
    __tablename__ = "Tablename"
    id = Column(Integer, primary_key=True)
    column_name = Column(<Type>)
    
    def __repr__(self):
        return f"<Tablename(column_name={self.column_name})>"
```


- [x] ~~write config.py~~ .env < DATABASE_URI + DONT FORGET ABOUT .GITIGNORE
```
# in .env file:
# Scheme: "postgresql+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"
DATABASE_URI=postgresql+psycopg2://postgres:nimda@localhost:5432/books

# in crud.py file later:
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URI = os.getenv("DATABASE_URI")
```


- [x] create an engine (crud.py | db.py) + connect to db
```
from sqlalchemy import create_engine
engine = create_engine(DATABASE_URI)
```


- [x] create a table: books (bookid, title, author, published, pages) 
? later add genres (genreid, bookid, genre)
```
from models import Base

def create_database():
    Base.metadata.create_all(engine)
```

- [x] create a session to interact with the new table
``` in crud.py file:
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

# later
s = Session()
s.close()
```

- copied books.yaml to insert it


- [x] insert data
```
recreate_database()
s = Session()
for data in yaml.load_all(open("books.yaml"), Loader=yaml.SafeLoader):
    book = Book(**data)
    s.add(book)

s.commit()

print(*s.query(Book).all(), sep="\n")

s.close()

# so, s = Session() > use model to store data > s.add(model) > s.commit() > s.close()
```

- [x] make several queries
```
# So, basically
# query == SELECT
# filter, filter_by == WHERE
# filter_by - for simpler queries
# filter - for complex queries, more verbose and more readable

print(*s.query(Book).all(), sep="\n")

r = s.query(Book).filter_by(title="Deep Learning").first()
r = s.query(Book).filter(Book.title == "Deep Learning").first()

# ilike == ILIKE
# ilike - works with filter !

r = s.query(Book).filter(Book.title.ilike('deep learning')).first()

# between == BETWEEN

start_date = datetime(2009, 1, 1)
end_date = datetime(2012, 1, 1)

s.query(Book).filter(Book.published.between(start_date, end_date)).all()

# and_, or_ need to be imported!

from sqlalchemy import and_, or_

r = s.query(Book).filter(
        and_(
            Book.pages > 750, 
            Book.published > datetime(2016, 1, 1)
            )
        ).all()
    
print("AND_:\n", r)

r = s.query(Book).filter(
        or_(
            Book.published < datetime(2010, 1, 1),
            Book.published > datetime(2016, 1, 1)
            )
        ).all()
print("OR_:\n", r)

r = s.query(Book).order_by(Book.pages.desc()).all()

print("order_by:\n", *r, sep="\n")

r = s.query(Book).order_by(Book.pages.desc()).limit(2).all()

print("limit 2:\n", r, "\n")

r = s.query(Book).order_by(Book.pages.desc()).limit(2).offset(2).all()

print("limit 2, offset 2:\n", r, "\n")

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

# BESIDES, it's possible to:
# s.query(Book)\
#    .filter(...)\
#    .filter(...)\
#    .order_by(...)\
#    .limit()\
#    .all()
```

- [ ] migrations?