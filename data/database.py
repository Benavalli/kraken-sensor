from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from data.tables import Measures, Events, Pictures
import os

def get_engine():
    engine_url = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'Kraken.db')
    engine = create_engine(engine_url)
    if not database_exists(engine_url):
        create_database(engine_url)
    return engine

def __create_tables(database):
    Measures.__table__.create(bind = database, checkfirst = True)
    Events.__table__.create(bind = database, checkfirst = True)
    Pictures.__table__.create(bind = database, checkfirst = True)

def persist_object(database, table_object):
    Session = sessionmaker(bind = database)
    session = Session()
    try:
        session.add(table_object)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
    finally:
        session.close()

__create_tables(get_engine())
