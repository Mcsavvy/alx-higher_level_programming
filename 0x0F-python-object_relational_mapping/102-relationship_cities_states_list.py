#!/usr/bin/python3

"""
A script that lists all states in the database.
"""

from relationship_city import Base, City
from relationship_state import State


if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    import sys

    host, password, name = sys.argv[1:]
    uri = f"mysql+mysqldb://{host}:{password}@localhost/{name}"
    engine = create_engine(uri, pool_pre_ping=True)

    session = sessionmaker(bind=engine)()
    query = (
        session.query(City).join(State)
        .order_by(City.id)
    )

    for city in query:
        print(f"{city.id}: {city.name} -> {city.state.name}")
