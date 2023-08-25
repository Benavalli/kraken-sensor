from sqlalchemy.orm import sessionmaker
from database_tables import Measures, Events, Pictures

Session = sessionmaker(bind=engine)
session = Session()

Measures(date = xxx, temperature = xxx, humidity = xxx)
Events(date = xxx, name = xxx)
Pictures(date = xxx, picture = xxx)