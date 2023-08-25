from sqlalchemy import Column, Integer, Sequence, String, DateTime, Float, BLOB
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Measures(Base):
    __tablename__ = 'measures'
    id = Column(Integer, Sequence('measures_seq'), primary_key = True)
    date = Column(DateTime)
    temperature = Column(Float)
    humidity = Column(Float)

class Events(Base):
    __tablename__ = 'events'
    id = Column(Integer, Sequence('events_seq'), primary_key = True)
    date = Column(DateTime)
    device = Column(String)
    state = Column(String)

class Pictures(Base):
    __tablename__ = 'pictures'
    id = Column(Integer, Sequence('picturesseq'), primary_key = True)
    date = Column(DateTime)
    picture = Column(BLOB)
