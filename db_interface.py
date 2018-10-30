from sqlalchemy import *
from sqlite3 import dbapi2 as sqlite
import matplotlib.pyplot as plt
import pandas as pd
import time
import datetime
from calculations import calculateSpeed, calculatePace, calculatePerformanceSpeed, convertStringToFloat
import sqlalchemy
from tabulate import tabulate

tb_sport = "sport"
tb_mountains = "mountains"
tb_runroutes = "runroutes"
tb_difficulty = "difficulty"
tb_tracksrun = "tracksrun"
tb_tracksalpine = "tracksalpine"
tb_rungoals = "rungoals"
tb_weight = "weight"

PATH_TO_DB = "C:/Dropbox/Gesundheit/App/CL/data/patfit.db"
connection_string = "sqlite+pysqlite:///{path_to_db}".format(path_to_db=PATH_TO_DB)
engine = create_engine(connection_string, module=sqlite)

#read whole table from DB
def readTableFromDB(db_table, db=engine, parse_dates=[], index_col="id", columns=None):    
    return pd.read_sql_table(db_table,db,index_col = index_col, columns=columns,parse_dates=parse_dates)

# add new track
def addTrack(running ):

    if running:
        # Ask for Date
        date = DateDuration()
        # Ask for route
        routes = readTableFromDB(tb_runroutes,engine,parse_dates=[])
        routeID, distance = selectRoute(routes)
        # Calculate pace
        pace = calculatePace(distance,date)
        # Calculate Speed from Pace
        speed = calculateSpeed(pace)
        # Create Dict
        newTrack = {"date_duration": date,
                    "runroute_id": routeID,
                    "pace": pace,
                    "speed": speed}
        # Convert Dict to Pandas Dataframe
        newTrack = pd.DataFrame(newTrack, index = [1])
        # Print what was entered
        print(tabulate(newTrack,headers = "keys",tablefmt="psql",showindex="never"))
        # Ask if User wants to save new running track
        i = input("Do you want to save the new running track (Y/N)? ")
        if i == "J" or i =="j" or i == "y" or i == "Y":
                newTrack.to_sql("tracksrun",engine,index=False,if_exists="append")
        pass
    else:
        # Ask for Date & Duration
        date = DateDuration()
        horizontalSeperator()    
        # Select mountain
        mountainID = selectMountain(engine)
        horizontalSeperator()
        # Enter if Summit was climbed or not
        summit = 2
        while summit != True and summit != False:
            summit = input("Does this include the summit? (Y/N)? ")
            if (summit == "J" or summit =="j" or summit == "y" or summit == "Y"):
                # Summit was climbed
                summit = True
            elif (summit == "N" or summit == "n"):
                # Summit was NOT climbed
                summit = False
            else:
                horizontalSeperator(string = "!")
                print("%s is an invalid Option. Try again!" % option)
        # Select Sport and Difficulty
        sportID = selectSport()
        difficultyID = selectDifficulty(sportID)
        horizontalSeperator()
        # Enter Conditions & Weather
        conditions = input("How were the conditions & weather? ")
        horizontalSeperator()  
        # Enter Horizontal Distance
        distance = input("Enter the horizontal distance in km: ")
        distance = convertStringToFloat(distance)
        # Enter Meters of Ascend
        ascend = input("Enter vertical meters ascend: ")
        ascend = int(ascend)
        # Enter Meters of Descend
        descend = input("Enter vertical meters descend: ")
        descend = int(descend)
        horizontalSeperator()  
        # Calculate Performance Speed
        performanceSpeed = calculatePerformanceSpeed(date, distance,ascend, descend)
        # Generate a Dict with input
        newTrack = {"mountain_id": mountainID,
                    "sport_id": sportID,
                    "difficulty_id": difficultyID,
                    "date_duration": date,
                    "conditions": conditions,
                    "summit": summit,
                    "distance": distance,
                    "ascend": ascend,
                    "descend": descend,
                    "performancespeed": performanceSpeed}
        # Convert Dict to Panda Dataframe
        newTrack = pd.DataFrame(newTrack, index = [1])
        # Print what was entered
        print(tabulate(newTrack,headers = "keys",tablefmt="psql",showindex="never"))
        # Ask if User wants to save new alpine track
        i = input("Do you want to save the new apline track (Y/N)? ")
        if i == "J" or i =="j" or i == "y" or i == "Y":
                newTrack.to_sql(tb_tracksalpine,engine,index=False,if_exists="append")
        pass

# Add a new Route for running
def addRouteRunning():
    print()
    # Ask for Name of Route
    name = input("Enter Name of Route: ")    
    # Ask for Location
    location = input("Enter Location: ")
    # Ask for distance of Route
    distance = input("Enter Distance of Route in km: ")
    # Convert distance to Float
    distance = convertStringToFloat(distance)
    # Create dict
    route = {"location": location,
              "name": name,
              "distance": distance } 
    # Convert dict to Panda Dataframe
    route = pd.DataFrame(route, index = [1])
    # Print what was entered
    print(tabulate(route,headers = "keys",tablefmt="psql",showindex="never"))
    # Ask if User wants to save new route
    i = input("Do you want to save the new running route (Y/N)? ")
    if i == "J" or i =="j" or i == "y" or i == "Y":
            route.to_sql(tb_runroutes,engine,index=False,if_exists="append")
    pass 

# add a goal
def addGoal ():

    distance_last_month =readTableFromDB(tb_tracksrun,engine,columns=["date_duration", "runroute_id"],parse_dates=["date_duration"])


    delta = input("How many kilometers do you want to run more than last month?")
    convertStringToFloat(delta)

    horizontalSeperator(string = "!")
    print("not implemented yet")
    horizontalSeperator(string = "!")
    pass

# add a alpine sport
def addSport():
    print()
    # Ask for Name of Sport
    sport = input("Enter Name of Sport: ")    
    # Creat Dict
    newSport = {"sport": sport} 
    # Convert Dict to Pandas Dataframe
    newSport = pd.DataFrame(newSport, index = [1])  
    # Print what was entered
    print(tabulate(newSport,headers = "keys",tablefmt="psql",showindex="never"))
    # Ask if User wants to save new sport
    i = input("Do you want to save the new sport (Y/N)? ")
    if i == "J" or i =="j" or i == "y" or i == "Y":
            newSport.to_sql(tb_sport,engine,index=False,if_exists="append")
    pass 

# add an difficulty
def addDifficulty():
    print()
    # Ask for SportID
    SportID = selectSport()
    # Ask for difficulty code
    difficulty = input("Enter Difficulty Code: ")
    # Ask for description
    description = input("Enter Description: ")
    # Create Dict
    newDifficulty = {"sport_id": SportID,
              "difficulty": difficulty,
              "description": description} 
    # Convert Dict to Pandas Dataframe
    newDifficulty = pd.DataFrame(newDifficulty, index = [1])
    # Print what was entered
    print(tabulate(newDifficulty,headers = "keys",tablefmt="psql",showindex="never"))
    # Ask if User wants to save new sport
    i = input("Do you want to save the new difficulty (Y/N)? ")
    if i == "J" or i =="j" or i == "y" or i == "Y":
            newDifficulty.to_sql(tb_difficulty,engine,index=False,if_exists="append")
    pass 

# add a mountain
def addMountain():
    print()
    # Ask for Name of Route
    name = input("Enter Name of Summit: ")    
    # Ask for Location
    countrycode = input("Enter Countrycode: ")
    # Ask for distance of Route
    mountainrange = input("Enter Mountainrange: ")
    # Ask for distance of Route
    elevation = input("Enter Elevation: ")    
    # Ask for distance of Route
    type = input("Enter Mountaintype (Pass, Berg, Vulkan): ")
    # Create Dict
    mountain = {"name": name,
              "countrycode": countrycode,
              "mountainrange": mountainrange,
              "elevation": elevation,
              "type": type} 
    # Convert Dict to Pandas Dataframe
    mountain = pd.DataFrame(mountain, index = [1])
    # Print what was entered
    print(tabulate(mountain,headers = "keys",tablefmt="psql",showindex="never"))
    # Ask if User wants to save new sport
    i = input("Do you want to save the new mountain (Y/N)? ")
    if i == "J" or i =="j" or i == "y" or i == "Y":
            mountain.to_sql(tb_mountains,engine,index=False,if_exists="append")
    pass 

# select a route
def selectRoute (routes_in):
    routes_in = readTableFromDB(tb_runroutes,engine)
    print(tabulate(routes_in,headers = "keys",tablefmt="psql"))
    selection = input("Select Route: ")
    selection = int(selection)
    distance = routes_in.loc[selection]
    return selection, distance.loc["distance"]

# select difficulty
def selectDifficulty (sport_id):
    difficulty = readTableFromDB(tb_difficulty,engine)
    difficultyBool = difficulty["sport_id"] == sport_id
    difficulty = difficulty[difficultyBool]
    print(tabulate(difficulty,headers = "keys",tablefmt="psql"))
    selection = input("Select difficulty: ")
    selection = int(selection)
    return selection

# select a alpine sport
def selectSport ():
    sports = readTableFromDB(tb_sport,engine,columns=["id","sport"],index_col="id")
    print(tabulate(sports,headers = "keys",tablefmt="psql"))
    selection = input("Select Sport: ")
    sportID = int(selection)
    return sportID

# select a mountain
def selectMountain(db):
    mountains = readTableFromDB(tb_mountains,db,index_col="id")
    mountainrange = pd.unique(mountains["mountainrange"])
    index = [int(i) for i in range(1, len(mountainrange)+1)]
    mountainrange = pd.DataFrame(mountainrange,index=index)
    mountainrange.columns = ["mountainrange"]
    print(tabulate(mountainrange,headers = "keys",tablefmt="psql"))
    selection = input("Select Mountainrange: ")
    selection = int(selection)
    selection -= 1
    mountainrange = mountainrange.iloc[selection]
    mountainrange = mountainrange.to_string(header=False,index=False)
    mountainrangeBool = mountains["mountainrange"]== mountainrange
    mountains = mountains[mountainrangeBool]
    print(tabulate(mountains,headers = "keys",tablefmt="psql"))
    selection = input("Select Mountain: ")
    selection = int(selection)

    return selection

# Check!!
def showMountainSummits():
    mountains = readTableFromDB(tb_mountains,engine,columns=["name","mountainrange"])
    alpineTracks = readTableFromDB(tb_tracksalpine,engine)
    print(tabulate(alpineTracks,headers = "keys",tablefmt="psql",showindex="never"))

    alpineTracks = alpineTracks["summit"==True]
    print(tabulate(alpineTracks,headers = "keys",tablefmt="psql",showindex="never"))
    
    pass

# User Input date and duration
def DateDuration():
    # Enter date
    while True:
        date_in = input("Enter Date (dd.mm.yyyy) [leave empty for today]: ")
        if date_in == "": 
            date_in = datetime.date.today()
            day = date_in.day
            month = date_in.month
            year = date_in.year
            print(date_in)
            break
        else:
            try:
                # Split entered date in day, month and year
                day, month, year = date_in.split(".")
                break
            except ValueError:
                horizontalSeperator(string = "!")
                print("Couldn't interpret date! Try again ...")

    # Enter Duration
    horizontalSeperator()    
    while True:
        duration_in = input("Enter Duration (hh:mm:ss): ")
        try:
            # Split Duration in hours, minutes and seconds
            hours, minutes, seconds = duration_in.split(":")
            if  minutes != "" and seconds != "" and hours == "":
                hours = 0
                break
            elif hours != "":
                break
            else:
                horizontalSeperator(string = "!")
                print("Couldnt interpret duration! Try again ...")
        except ValueError:
            horizontalSeperator(string = "!")
            print("Couldnt interpret duration! Try again ...")

    # convert all Date/Time Variables to int
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)
    day = int(day)
    month =int(month)
    year = int(year)

    # Return a datetime
    return datetime.datetime(year, 
                             month, 
                             day, 
                             hours,
                             minutes,
                             seconds)

def horizontalSeperator(string = "-",length = 42):
    print("+" + (string*(length//len(string)+1))[:length] + "+")
    pass

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class RunTrack(Base):
    __tablename__='tracksrun'
    id = Column('id', Integer, primary_key=True)
    date_duration = Column('date_duration',DateTime, nullable = False)
    runroute_id = Column('runroute_id', Integer,ForeignKey('runroutes.id'), nullable = False)
    #route = Relationship("RunRoutes")

    pace = Column('pace', Float, nullable = False)
    speed = Column('speed', Float, nullable = False)
    

class AlpineTrack(Base):
    __tablename__ = "tracksalpine"
    id = Column("id", Integer, primary_key=True)
    mountain_id = Column("mountain_id", Integer, ForeignKey("mountains.id"), nullable=False)
    sport_id = Column("sport_id", ForeignKey("sport.id"), nullable =False)
    difficulty_id = Column("difficulty_id", ForeignKey("difficulty.id"), nullable = False)
    date_duration = Column("date_duration", nullable = False)
    conditions = Column("conditions", Text)
    summit = Column("summit", Boolean, nullable = False)
    distance = Column("distance", Float, nullable = False)
    ascend = Column("ascend", Integer, nullable = False)
    descend =Column("descend", Integer, nullable = False)
    performancespeed = Column("performanceSpeed", Float, nullable = False)

class RunRoutes(Base):
    __tablename__ = "runroutes"

    id = Column("id",Integer, primary_key=True)
    name = Column("name",String(50), nullable=False)
    location = Column("location",String(30), nullable=False)
    distance = Column("distance",Float, nullable=False)