from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


Base = declarative_base()
engine = create_engine('sqlite:///address_book.db', echo=False)
DBSession = sessionmaker(bind=engine)
session = DBSession()

