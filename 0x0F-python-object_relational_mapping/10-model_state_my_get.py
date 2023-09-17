#!/usr/bin/python3
"""
script that prints the State object with the name passed as argument
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
    searched_object = session.query(State).order_by(State.id)\
        .filter(State.name.like(sys.argv[4])).all()
    if searched_object:
        for object in searched_object:
            print(object.id)
    else:
        print("Not found")
    session.close()
