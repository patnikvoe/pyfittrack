import matplotlib.pyplot as plt
import pandas as pd
import time
import datetime
#from calculations import calculateSpeed, calculatePace, calculatePerformanceSpeed, convertStringToFloat
import sqlalchemy
from tabulate import tabulate

from sqlalchemy import *
# Database connection
from classes import Base, Engine, Session, session
# Table Names
#from classes import tb_sport, tb_mtype, tb_users, tb_weight, tb_routes,\
#    tb_country, tb_rungoals, tb_tracksrun, tb_mountains, tb_runroutes,\
#    ⁠tb_difficulty, tb_tracksalpine

#read whole table from DB
def readTableFromDB(db_table, db=Engine, parse_dates=[], index_col="id", columns=None):
    return pd.read_sql_table(db_table,db,index_col = index_col, columns=columns,parse_dates=parse_dates)

# Add new entry to Database
def saveNewInput(type,object):
    while True:
        i = input("Do you want to save the new %s (Y/N)? "%(type))
        if i == "J" or i =="j" or i == "y" or i == "Y":
            moveToDatabase(object)
            break
        else if i=="n" or i=="N":
            break
        else
            print("Invalid Input! Try again!")
        pass


# Add new entry to Database
def moveToDatabase(name):
    session.add(name)
    session.commit()

# select a route
def selectRoute (routes_in):
    routes_in = readTableFromDB(tb_runroutes,Engine)
    print(tabulate(routes_in,headers = "keys",tablefmt="psql"))
    selection = input("Select Route: ")
    selection = int(selection)
    distance = routes_in.loc[selection]
    return selection, distance.loc["distance"]

# select difficulty
def selectDifficulty (sport_id):
    difficulty = readTableFromDB(tb_difficulty,Engine)
    difficultyBool = difficulty["sport_id"] == sport_id
    difficulty = difficulty[difficultyBool]
    print(tabulate(difficulty,headers = "keys",tablefmt="psql"))
    selection = input("Select difficulty: ")
    selection = int(selection)
    return selection

# select a alpine sport
def selectSport ():
    sports = readTableFromDB(tb_sport,Engine,columns=["id","sport"],index_col="id")
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
    mountains = readTableFromDB(tb_mountains,Engine,columns=["name","mountainrange"])
    alpineTracks = readTableFromDB(tb_tracksalpine,Engine)
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
