#!/usr/bin/python3

"""
A script that lists all states in the database.
"""

from model_city import Base, State, City


if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    import sys

    host, password, name = sys.argv[1:]
    uri = f"mysql+mysqldb://{host}:{password}@localhost/{name}"
    engine = create_engine(uri, pool_pre_ping=True)

    session = sessionmaker(bind=engine)()
    query = session.query(State).join(City).order_by(City.id)

    for state in query:
        for city in state.cities:
            print(f"{state.name}: ({city.id}) {city.name}")
