from model import Base, Users , books
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_user(username):
	user_object=Users(
		username=username
	)
	session.add(user_object)
	session.commit()


def add_review(name, review):
	name_object=books(
		name=name , review=review
	)
	session.add(name_object)
	session.commit()





