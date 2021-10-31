from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key = True)
  username = Column(String)


class books(Base):
  __tablename__ = 'books'
  id = Column(Integer, primary_key = True)
  name = Column(String)
  review = Column(String)




  
