#!/usr/bin/python3
"""
script that lists all City objects from the database hbtn_0e_14_usa
"""
if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_city import Base, City
    from model_state import Base, State
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format("root", "root", sys.argv[3]),
                           pool_pre_ping=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    joined_data = session.query(State, City)\
        .join(City, State.id == City.state_id).all()
    for state, city in joined_data:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
