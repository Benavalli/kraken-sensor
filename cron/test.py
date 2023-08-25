from database import database
from datetime import datetime
from database.tables import Measures

engine = database.get_engine()
measure = Measures(date = datetime.now(), temperature = 23.4, humidity = 22.0)
database.persist_object(measure)
