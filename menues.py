from sys import platform
from db_interface import horizontalSeperator
from db_interface import showMountainSummits
from plots import plot_goal_actuall
from db_interface import addTrack, addRouteRunning, readTableFromDB, addMountain, addSport, addDifficulty
import pandas as pd
import os
from time import sleep

from sqlalchemy import *
from sqlalchemy import create_engine
from sqlite3 import dbapi2 as sqlite
import matplotlib.pyplot as plt
import pandas as pd
import time
import datetime
from tabulate import tabulate

PATH_TO_DB = "C:/Dropbox/Gesundheit/App/CL/data/patfit.db"
connection_string = "sqlite+pysqlite:///{path_to_db}".format(path_to_db=PATH_TO_DB)
engine = create_engine(connection_string, module=sqlite)

tb_sport = "sport"
tb_mountains = "mountains"
tb_runroutes = "runroutes"
tb_difficulty = "difficulty"
tb_tracksrun = "tracksrun"
tb_tracksalpine = "tracksalpine"
tb_rungoals = "rungoals"
tb_weight = "weight"

if platform == "linux" or platform == "linux2" or platform == "darwin":
    # linux and mac
    clear = lambda: os.system("clear") #on Linux System
elif platform == "win32":
    # Windows...
    clear = lambda: os.system("cls") #on Windows System

def menumain():
    print()
    print("Main Menu")
    options = {"#": [1,
                     2,
                     3,
                     "",
                     0],
               "Option": ["Add Menu", 
                          "Show Data", 
                          "Analysis Menu",
                          "-------------",                          
                          "Exit Programm"]}
    print(tabulate(options,headers = "keys",tablefmt="psql",showindex="never"))
    while True:
        option = input("Option: ")
        try:
            option = int(option)
            if option <= len(options["#"])-2 and option >= 0:
                break
            else:
                horizontalSeperator(string = "!")
                print("%s is an invalid Option. Try again!" % option)
        except ValueError:
            horizontalSeperator(string = "!")
            print("%s is an invalid Option. Try again!" % option)
    clear()
    print()
    if option == 1:
        addMenu()
    elif option == 2:
        showTablesMenu()
    elif option == 3:
        analysisMenu()
    elif option == 0:
        horizontalSeperator()
        print("Closing programm")
        horizontalSeperator()
        sleep(1)
        quit()    

def addMenu():
    while True:
        print()
        print("Add Menu")
        options = {"#": [1,
                         2,
                         3,
                         4,
                         5,
                         6,
                         7,
                         8,
                         "",
                         0],
                   "Option": ["Add new running track", 
                              "Add new alpine track", 
                              "Add new running route", 
                              "Add new goals",
                              "Add new mountain",
                              "Add new sport",
                              "Add new difficulty",
                              "Add new weight",
                              "---------------------",
                              "Back to main menu"]}
        print(tabulate(options,headers = "keys",tablefmt="psql",showindex="never"))
        while True:
            option = input("Option: ")
            try:
                option = int(option)
                if option <= len(options["#"])-2 and option >= 0:
                    break
                else:
                    horizontalSeperator(string = "!")
                    print("%s is an invalid Option. Try again!" % option)
            except ValueError:
                horizontalSeperator(string = "!")
                print("%s is an invalid Option. Try again!" % option)
        clear()
        print()
        if option == 1: 
            print("Add new running track")
            previousEntries = readTableFromDB(tb_tracksrun,engine, parse_dates=["dateduration"])
            previousEntries = previousEntries.sort_values(by=["date_duration"])
            print(tabulate(previousEntries[-5:],headers = "keys",tablefmt="psql"))
            addTrack(True)
        elif option == 2: 
            print("Add new alpine track")
            previousEntries = readTableFromDB(tb_tracksalpine,engine,columns=["mountain_id", "sport_id", "date_duration", "summit","performancespeed"],parse_dates=["date_duration"])
            previousEntries = previousEntries.sort_values(by=["date_duration"])
            print(tabulate(previousEntries[-5:],headers = "keys",tablefmt="psql"))
            addTrack(False)
        elif option == 3:
            print("Add new running route")
            print(tabulate(readTableFromDB(tb_runroutes,engine),headers = "keys",tablefmt="psql"))
            addRouteRunning()
        elif option == 4:
            print("Add new goals")
            print(tabulate(readTableFromDB(tb_rungoals,engine,parse_dates=["date"]),headers = "keys",tablefmt="psql"))
        elif option == 5:
            print("Add new mountain")
            print(tabulate(readTableFromDB(tb_mountains,engine),headers = "keys",tablefmt="psql"))
            addMountain()
        elif option == 6:
            print("Add new sport")
            print(tabulate(readTableFromDB(tb_sport,engine),headers = "keys",tablefmt="psql"))
            addSport()
        elif option == 7:
            print("Add new difficulty")
            print(tabulate(readTableFromDB(tb_difficulty,engine),headers = "keys",tablefmt="psql"))
            addDifficulty()
        elif option == 8: 
            print("Add new weight")
            print(tabulate(readTableFromDB(tb_weight,engine,parse_dates=["date"]),headers = "keys",tablefmt="psql"))
        elif option == 0:
            clear()
            break

def showTablesMenu():
    while True:
        print()
        print("Show Data Menu")
        options = {"#": [1,
                         2,
                         3,
                         4,
                         5,
                         6,
                         7,
                         8,
                         "",
                         0],
                   "Option": ["Show running track", 
                              "Show alpine track", 
                              "Show running route", 
                              "Show goals",
                              "Show mountain",
                              "Show sport",
                              "Show difficulty",
                              "Show weight",
                              "------------------",
                              "Back to main menu"]}
        print(tabulate(options,headers = "keys",tablefmt="psql",showindex="never"))
        while True:
            option = input("Option: ")
            try:
                option = int(option)
                if option <= len(options["#"])-2 and option >= 0:
                    break
                else:
                    horizontalSeperator(string = "!")
                    print("%s is an invalid Option. Try again!" % option)
            except ValueError:
                horizontalSeperator(string = "!")
                print("%s is an invalid Option. Try again!" % option)
        clear()
        print()
        if option == 1:
            print("Running Tracks:")
            tracks = readTableFromDB(tb_tracksrun,engine)
            tracks = tracks.sort_values(by=["date_duration"])
            print(tabulate(tracks,headers = "keys",tablefmt="psql"))
            
            # Calculate the meanspeed
            meanspeed = tracks["speed"].mean()

            # Calculate the mean pace and display both means
            means = {"mean of": ["pace","speed"],
                     "value": [tracks["pace"].mean(), meanspeed],
                     "units": ["min/km","km/h"]}
            print(tabulate(means,headers = "keys",tablefmt="psql"))
            
            # Summing all times            
            runningTime = 0.0
            for index, row in tracks.iterrows():
                hours = row["date_duration"].hour
                minutes = row["date_duration"].minute
                seconds = row["date_duration"].second
                runningTime = runningTime + hours + (minutes + seconds/60)/60
            
            # calculating distance and display it
            distance = {"Total Distance [km]": [runningTime*meanspeed]}
            print(tabulate(distance,headers = "keys",tablefmt="psql"))

        elif option == 2:
            print("Alpine Tracks:")
            tracks = readTableFromDB(tb_tracksalpine,engine,columns=["date_duration","sport_id","mountain_id","distance","ascend","descend","performancespeed"])
            tracks = tracks.sort_values(by=["date_duration"])
            print(tabulate(tracks,headers = "keys",tablefmt="psql"))
        elif option == 3:
            print("Running Routes:")
            routes = readTableFromDB(tb_runroutes,engine)
            print(tabulate(routes,headers = "keys",tablefmt="psql"))
        elif option == 4:
            print("Goals:")
            print(tabulate(readTableFromDB(tb_rungoals,engine,columns=["date","distancegoal"]),headers = "keys",tablefmt="psql"))
        elif option == 5:
            print("Mountains:")
            mountains = readTableFromDB(tb_mountains,engine,columns=["name","countrycode","elevation","type"])
            print(tabulate(mountains.sort_values(by=["name"]),headers = "keys",tablefmt="psql"))
        elif option == 6:
            print("Sports:")
            sports = readTableFromDB(tb_sport,engine)
            sports = sports.sort_values(by=["sport"])
            print(tabulate(sports,headers = "keys",tablefmt="psql"))
        elif option == 7:
            print("Difficulties:")
            print(tabulate(readTableFromDB(tb_difficulty,engine),headers = "keys",tablefmt="psql"))
        elif option == 8:
            print("Weight:")
            weight = readTableFromDB(tb_weight,engine)
            weight = weight.sort_values(by=["date"])
            print(tabulate(weight, headers = "keys",tablefmt="psql"))
        elif option == 0:
            clear()
            break
        
def analysisMenu():
    while True:
        print()
        print("Analysis Menu")
        options = {"#": [1,
                         2,
                         3,
                         4,
                         5,
                         "",
                         0],
                   "Option": ["Show Mountains with Summits", 
                              "Analysis for skitouring", 
                              "Analysis for hiking", 
                              "Analysis for running",
                              "Weight Analysis",
                              "---------------------------",
                              "Back to main menu"]}
        print(tabulate(options,headers = "keys",tablefmt="psql",showindex="never"))
        while True:
            option = input("Option: ")
            try:
                option = int(option)
                if option <= len(options["#"])-2 and option >= 0:
                    break
                else:
                    horizontalSeperator(string = "!")
                    print("%s is an invalid Option. Try again!" % option)
            except ValueError:
                horizontalSeperator(string = "!")
                print("%s is an invalid Option. Try again!" % option)
        clear()
        print()
        if option == 1:
            print("Show Mountain with Summits")
            #showMountainSummits(engine)
            #horizontalSeperator()
        elif option == 2:
            print("Analysis for skitouring")
        elif option == 3:
            print("Analysis for hiking")
        elif option == 4:
            print("Analysis for running")
        elif option == 5:
            print("Weight Analysis")
        elif option == 0:
            clear()
            break