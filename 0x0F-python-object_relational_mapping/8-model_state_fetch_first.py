#!/usr/bin/python3
"""
script that lists first State objects from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format("root", "root", sys.argv[3]),
                           pool_pre_ping=False)
    Base.metadata.create_all(engine)
    session = Session(engine)
    first_object = session.query(State).order_by(State.id).first()
    if first_object:
        print("{}: {}".format(first_object.id, first_object.name))
    else:
        print("Nothing")
    session.close()
