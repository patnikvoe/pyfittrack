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
import pandas as pd

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

# id Names
user_id = "user_id_seq"
sport_id = "sport_id_seq"
mountains_id = "mountains_id_seq"
routes_id = "routes_id_seq"
difficulty_id = "difficulty_id_seq"
tracksrun_id = "tracksrun_id_seq"
tracksalpine_id = "tracksalpine_id_seq"
rungoals_id = "rungoals_id_seq"
weight_id = "weight_id_seq"
mtype_id = "mtype_id_seq"
country_id = "country_id_seq"
users_id = "users_id_seq"
