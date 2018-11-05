from sys import platform
from classes.plots import plot_goal_actuall
from classes.functions import readTableFromDB, horizontalSeperator
import pandas as pd
import os
from time import sleep
from pyfittrack import clear
from sqlalchemy import *
from sqlalchemy import create_engine
from sqlite3 import dbapi2 as sqlite
import matplotlib.pyplot as plt
import time
import datetime
from tabulate import tabulate

from classes.classes import AlpineTrack
from classes.classes import Country
from classes.classes import Difficulty
from classes.classes import Mountain
from classes.classes import MountainType
from classes.classes import RouteRun
from classes.classes import Sport
from classes.classes import TrackRun
from classes.classes import User
from classes.classes import Weight

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
            previousEntries = readTableFromDB(tb_tracksrun,engine, parse_dates=["DateDuration"])
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
                         "",
                         0],
                   "Option": ["Show running track",
                              "Show alpine track",
                              "Show running route",
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
            tracks = TrackRun.queryAll()
            print(tabulate(tracks,headers = "keys",tablefmt="psql"))

            # # Calculate the meanspeed
            # meanspeed = tracks["speed"].mean()
            #
            # # Calculate the mean pace and display both means
            # means = {"mean of": ["pace","speed"],
            #          "value": [tracks["pace"].mean(), meanspeed],
            #          "units": ["min/km","km/h"]}
            # print(tabulate(means,headers = "keys",tablefmt="psql"))

            # Summing all times
            # runningTime = 0.0
            # for index, row in tracks.iterrows():
            #     hours = row["date_duration"].hour
            #     minutes = row["date_duration"].minute
            #     seconds = row["date_duration"].second
            #     runningTime = runningTime + hours + (minutes + seconds/60)/60
            #
            # # calculating distance and display it
            # distance = {"Total Distance [km]": [runningTime*meanspeed]}
            # print(tabulate(distance,headers = "keys",tablefmt="psql"))

        elif option == 2:
            print("Alpine Tracks:")
            tracks = AlpineTrack.queryAll()
            print(tabulate(tracks,headers = "keys",tablefmt="psql"))
        elif option == 3:
            print("Running Routes:")
            routes = RouteRun.queryAll()
            print(tabulate(routes,headers = "keys",tablefmt="psql"))
        elif option == 4:
            print("Mountains:")
            mountains = Mountain.queryAll()
            mountains = mountains.sort_values(by=["name"])
            print(tabulate(mountains,headers = "keys",tablefmt="psql"))
        elif option == 5:
            print("Sports:")
            sports = Sport.queryAll()
            sports = sports.sort_values(by=["sport"])
            print(tabulate(sports,headers = "keys",tablefmt="psql"))
        elif option == 6:
            dif = Difficulty.queryAll()
            print("Difficulties:")
            print(tabulate(dif,headers = "keys",tablefmt="psql"))
        elif option == 7:
            print("Weight:")
            weight = Weight.queryAll()
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
