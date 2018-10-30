from sqlite3 import dbapi2 as sqlite
from sqlalchemy import Table, Column, Boolean, Integer, String, Text, Time, Float, MetaData, Date, ForeignKey, create_engine, DateTime
import pandas as pd

PATHSQLITE = "C:/Dropbox/Gesundheit/App/CL/data/"
FILESQLITE = "patfit.db"

connection_string = "sqlite+pysqlite:///{path}{file}".format(
                        path=PATHSQLITE,
                        file=FILESQLITE)

engine = create_engine(connection_string, module=sqlite)


metadata = MetaData()

sport = Table("sport", metadata, 
                Column("id", Integer, primary_key = True),
                Column("sport", String(30), nullable=False),
                sqlite_autoincrement=True)

difficulty = Table("difficulty", metadata, 
                    Column("id", Integer, primary_key = True),
                    Column("sport_id", None, ForeignKey("sport.id"), nullable=False),
                    Column("difficulty", String(10), nullable=False),
                    Column("description", Text),
                    sqlite_autoincrement=True)

runroutes = Table("runroutes", metadata,
                    Column("id", Integer, primary_key=True),
                    Column("name", String(50), nullable=False),
                    Column("location", String(30), nullable=False),
                    Column("distance", Float, nullable=False),
                    sqlite_autoincrement=True)

tracksrun = Table("tracksrun", metadata,
                    Column("id", Integer, primary_key=True),
                    Column("date_duration", DateTime, nullable=False),
                    Column("runroute_id", None, ForeignKey("runroutes.id")),
                    Column("pace", Float),
                    Column("speed", Float),
                    sqlite_autoincrement=True)

mountains = Table("mountains", metadata,
                    Column("id", Integer, primary_key=True),
                    Column("name", String(80), nullable=False),
                    Column("countrycode", String(5), nullable =False),
                    Column("mountainrange", String(50)),
                    Column("elevation", Integer, nullable =False),
                    Column("type", String(20), nullable =False),
                    sqlite_autoincrement=True)

tracksalpine = Table("tracksalpine", metadata,
                    Column("id", Integer, primary_key=True),
                    Column("mountain_id", ForeignKey("mountains.id"), nullable=False),
                    Column("sport_id", ForeignKey("sport.id"), nullable =False),
                    Column("difficulty_id", ForeignKey("difficulty.id"), nullable = False),
                    Column("date_duration", DateTime, nullable = False),
                    Column("conditions", Text),
                    Column("summit", Boolean, nullable = False),
                    Column("distance", Float, nullable = False),
                    Column("ascend", Integer, nullable = False),
                    Column("descend", Integer, nullable = False),
                    Column("performancespeed", Float),
                    sqlite_autoincrement=True)

rungoals = Table("rungoals", metadata,
                    Column("id", Integer, primary_key=True),
                    Column("date", Date, nullable=False),
                    Column("distancegoal",Float, nullable = False),
                    Column("pacegoal", Float),
                    Column("speedgoal", Float),
                    sqlite_autoincrement=True)

weight = Table("weight", metadata,
               Column("id", Integer, primary_key=True),
               Column("date", Date, nullable=False),
               Column("weight",Float, nullable = False),
               Column("stomach_circumference", Float, nullable =False ),
               Column("neck_circumference", Float, nullable = False),
               Column("bodyfat_navy", Float, nullable = False),
               sqlite_autoincrement=True)

metadata.create_all(engine)

print("Finished creating database")