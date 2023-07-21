# TO DO
## thoughts

- should have added .gitignore for config.py (https://12factor.net/ru/config)
- decided to go with python-dotenv and .env file
- https://habr.com/ru/companies/ruvds/articles/521602/ - read later


## checklist
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


- [ ] insert data


- [ ] make several queries


- [ ] migrations?