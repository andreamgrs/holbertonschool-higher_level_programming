#!/usr/bin/python3
"""
Script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa

"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_name = sys.argv[4]
    # Use first not all if you want to get one object not a list
    state = (session.query(State).filter(State.name == state_name).first())
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
    session.close()
