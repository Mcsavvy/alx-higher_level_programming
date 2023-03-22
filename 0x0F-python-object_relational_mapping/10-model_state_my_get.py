#!/usr/bin/python3

"""
A script that prints the id of the state in the database
whose name matches a commandline argument passed in.
"""

from model_state import Base, State

if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    import sys

    host, password, name, search = sys.argv[1:]
    uri = f"mysql+mysqldb://{host}:{password}@localhost/{name}"
    engine = create_engine(uri, pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    search = search.split()[0].strip("\"';")
    query = session.query(State).filter(State.name == search)
    state = query.first()
    if state:
        print(state.id)
    else:
        print("Not found")
