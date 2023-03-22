#!/usr/bin/python3

"""
A script that lists all states in the database.
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

    for state in session.query(State).order_by(State.id):
        print(f"{state.id}: {state.name}")
