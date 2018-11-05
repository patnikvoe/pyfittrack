import matplotlib.pyplot as plt
import pandas as pd
import time
import datetime
import sqlalchemy
from tabulate import tabulate

# Database connection
from classes import Base, Engine, Session, session

#################################################################################
# Convert an string to float
def convertStringToFloat(input):
    # Check if entered with Comma -> replace if so
    if input.find(",",0,len(input))>0:
        input = input.replace(",",".")
    # convert distance to float
    return float(input)

#################################################################################
# Error message for invalid input
def invalidInput():
    horizontalSeperator()
    print("Invalid Input! Try again!")
    pass

#################################################################################
# Horizontal Seperator
def horizontalSeperator(string = "-",length = 42):
    print("+" + (string*(length//len(string)+1))[:length] + "+")
    pass

#################################################################################
# User Input date and duration
def enterDateDuration():
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

#################################################################################
# User input for Date only
def enterDate():
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

    day = int(day)
    month =int(month)
    year = int(year)
    return datetime.date(year, month, day)

#################################################################################
# Add new entry to Database
def saveNewInput(type,object):
    while True:
        i = input("Do you want to save the new %s (Y/N)? "%(type))
        if i == "J" or i =="j" or i == "y" or i == "Y":
            moveToDatabase(object)
            break
        elif i=="n" or i=="N":
            break
        else:
            print("Invalid Input! Try again!")
        pass

#################################################################################
# Add new entry to Database
def moveToDatabase(name):
    session.add(name)
    session.commit()

#################################################################################
#read whole table from DB
def readTableFromDB(db_table, db=Engine, parse_dates=[], index_col="id", columns=None):
    return pd.read_sql_table(db_table,db,index_col = index_col, columns=columns,parse_dates=parse_dates)
