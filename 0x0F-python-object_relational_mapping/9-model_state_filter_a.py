#!/usr/bin/python3
"""
script that lists first State objects that contain the letter a
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
    specific_object = session.query(State)\
        .order_by(State.id)\
        .filter(State.name.like('%a%')).all()
    for object in specific_object:
        print(f"{object.id}: {object.name}")
    session.close()
