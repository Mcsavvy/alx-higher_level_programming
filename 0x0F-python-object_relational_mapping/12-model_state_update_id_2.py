#!/usr/bin/python3

"""
A script that updates a state's name to "New Mexico"
"""

from model_state import Base, State

if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    import sys

    host, password, name = sys.argv[1:]
    uri = f"mysql+mysqldb://{host}:{password}@localhost/{name}"
    engine = create_engine(uri, pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    query = session.query(State).filter(State.id == 2)
    state = query.first()
    state.name = "New Mexico"
    session.commit()
