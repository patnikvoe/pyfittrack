__all__ = [
        'AlpineTrack',
        'Country',
        'Difficulty',
        'Mountain',
        'MountainType',
        'RouteRun',
        'Sport',
        'TrackRun',
        'User',
        'Weight'
        ]

from sqlalchemy import Column, create_engine, Integer, Sequence, DateTime, Text, Boolean, Float, ForeignKey, String, Date
#from sqlite3 import dbapi2 as sqlite
import psycopg2
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime
import time
from math import log10

Engine = create_engine("postgresql://pyfittracker:Fuss93ball6@localhost:5432/pyfittracker")
Base = declarative_base()
Session = sessionmaker(bind=Engine)
session = Session()

# Columns in Database
tb_sport = "sport"
tb_mountains = "mountains"
tb_routes = "routes"
tb_difficulty = "difficulty"
tb_tracksrun = "tracksrun"
tb_tracksalpine = "tracksalpine"
tb_rungoals = "rungoals"
tb_weight = "weight"
tb_mtype = "mtype"
tb_country = "country"
tb_users = "users"
