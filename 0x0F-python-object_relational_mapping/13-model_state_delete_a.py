#!/usr/bin/python3
"""
script that deletes all State objects
with a name containing the letter a
"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format("root", "root", sys.argv[3]),
                           pool_pre_ping=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    del_state = session.query(State)\
        .filter(State.name.like('%a%')).all()
    for state in del_state:
        session.delete(state)
    session.commit()
    session.close()
