#!/usr/bin/python3

"""
A script that prints the first state in the database.
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
    query = session.query(State)
    state = query.first()
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")
