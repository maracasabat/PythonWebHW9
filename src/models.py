from sqlalchemy import Column, Integer, String

from src.db import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    phone = Column('phone', String(20), nullable=False)
    email = Column('email', String(100), nullable=True)
    address = Column('address', String(120), nullable=True)
