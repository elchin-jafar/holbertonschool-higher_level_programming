#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter a
from database `hbtn_0e_6_usa`
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                           argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        for instance in session.query(State).filter(State.name.contains("a")):
            session.delete(instance)
    except Exception as e:
        print(e.args[0])

    session.commit()
    session.close()
