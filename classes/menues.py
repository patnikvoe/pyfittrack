# import from plots
from classes.plots import plot_goal_actuall

# import classes
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

#import database connection
from classes import Base, Engine, session, Session

#import from classes init
from classes import descriptionWrap, pd, time, datetime, tabulate, plt, sleep

#import custom functions from classes
from classes.functions import *

####################################################################################
####################################################################################
####################################################################################
# Main Menu
def menumain():
    clear()
    print()
    printTitle("Main Menu")
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
    printMenu(options)
    while True:
        option = input("Option: ")
        try:
            option = int(option)
            if option <= len(options["#"])-2 and option >= 0:
                break
            else:
                invalidInput()
        except ValueError:
            invalidInput()
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
        clear()
        quit()

####################################################################################
####################################################################################
####################################################################################
# Add Menu
def addMenu():
    clear()
    print()
    while True:
        printTitle("Add Menu")
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
        printMenu(options)
        while True:
            option = input("Option: ")
            try:
                option = int(option)
                if option <= len(options["#"])-2 and option >= 0:
                    break
                else:
                    invalidInput()
            except ValueError:
                invalidInput()
        clear()
        print()
        if option == 1:
            print("Add new running track")
            previousEntries = readTableFromDB(tb_tracksrun,engine, parse_dates=["DateDuration"])
            previousEntries = previousEntries.sort_values(by=["date_duration"])
            printPanda(previousEntries[-5:])
            addTrack(True)
        elif option == 2:
            print("Add new alpine track")
            previousEntries = readTableFromDB(tb_tracksalpine,engine,columns=["mountain_id", "sport_id", "date_duration", "summit","performancespeed"],parse_dates=["date_duration"])
            previousEntries = previousEntries.sort_values(by=["date_duration"])
            printPanda(previousEntries[-5:])
            addTrack(False)
        elif option == 3:
            print("Add new running route")
            printPanda(readTableFromDB(tb_runroutes,engine))
            addRouteRunning()
        elif option == 4:
            print("Add new goals")
            printPanda(readTableFromDB(tb_rungoals,engine,parse_dates=["date"]))
        elif option == 5:
            print("Add new mountain")
            printPanda(readTableFromDB(tb_mountains,engine))
            addMountain()
        elif option == 6:
            print("Add new sport")
            printPanda(readTableFromDB(tb_sport,engine))
            addSport()
        elif option == 7:
            print("Add new difficulty")
            printPanda(readTableFromDB(tb_difficulty,engine))
            addDifficulty()
        elif option == 8:
            print("Add new weight")
            printPanda(readTableFromDB(tb_weight,engine,parse_dates=["date"]))
        elif option == 0:
            clear()
            break

####################################################################################
####################################################################################
####################################################################################
# Show Entries Menu
def showTablesMenu():
    clear()
    print()
    while True:
        printTitle("Show Data Menu")
        options = {"#": [1,
                         2,
                         3,
                         4,
                         5,
                         6,
                         7,
                         8,
                         9,
                         "",
                         0],
                   "Option": ["Show running track",
                              "Show running route",
                              "Show alpine track",
                              "Show mountain",
                              "Show mountain types",
                              "Show sport",
                              "Show difficulty",
                              "Show weight",
                              "Show users",
                              "------------------",
                              "Back to main menu"]}
        printMenu(options)
        while True:
            option = input("Option: ")
            try:
                option = int(option)
                if option <= len(options["#"])-2 and option >= 0:
                    break
                else:
                    invalidInput()
            except ValueError:
                invalidInput()
        clear()
        print()
        if option == 1:
            printTitle("Running Tracks")
            tracks = TrackRun.queryAll()
            printPanda(tracks)

            # # Calculate the meanspeed
            # meanspeed = tracks["speed"].mean()
            #
            # # Calculate the mean pace and display both means
            # means = {"mean of": ["pace","speed"],
            #          "value": [tracks["pace"].mean(), meanspeed],
            #          "units": ["min/km","km/h"]}
            # printPanda(means)

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
            # printPanda(distance)

        ##################################################################################
        # works as expected
        elif option == 2:
            printTitle("Running Routes")
            routes = RouteRun.queryAll()
            routes.columns = ["Name", "Location", "Distance"]
            printPanda(routes)
            print()
        elif option == 3:
            printTitle("Alpine Tracks")
            tracks = AlpineTrack.queryAll()
            printPanda(tracks)
        elif option == 4:
            printTitle("Mountains")
            mountains = Mountain.queryAll()
            mountains = mountains.sort_values(by=["name"])
            printPanda(mountains)
        elif option == 5:
            printTitle("Mountain Types")
            mountains = Mountain.queryAll()
            mountains = mountains.sort_values(by=["name"])
            printPanda(mountains)
        elif option == 6:
            printTitle("Sports")
            sports = Sport.queryAll()
            sports = sports.sort_values(by=["Sport"])
            printPanda(sports)
            print()
        ##################################################################################
        # works as expected
        elif option == 7:
            printTitle("Difficulties")
            horizontalSeperator(length=descriptionWrap.width)
            dif = Difficulty.queryAll()
            dif = dif.sort_values(["sport_id","code"])
            for index, row in dif.iterrows():
                row["sport_id"] = Sport.selectName(row["sport_id"])
                string = "| %s | Code: %s | ID: %d | Description:"  %(row["sport_id"], row["code"], index)
                print(string)
                horizontalSeperator(length=len(string)-15)
                print("%s" %(descriptionWrap.fill(row["description"])))
                horizontalSeperator(length=descriptionWrap.width)
            print()
        ##################################################################################
        # works as expected
        elif option == 8:
            printTitle("Weight")
            we = Weight.queryAll()
            users = User.queryAll()
            we["username"] = we.user_id.map(users.name.to_dict())
            we["male"] = we.user_id.map(users.male.to_dict())
            we = we.sort_values(["user_id","date"])
            for index, row in we.iterrows():
                # check if new User started and print out the Username if so
                if index == 1:
                    string = "{0}".format(we.at[index, "username"])
                    printTitle(string)
                    horizontalSeperatorWeight(we.at[index, "male"])
                elif we.at[index, "username"] != we.at[index-1,"username"]:
                    horizontalSeperatorWeight(we.at[index-1, "male"])
                    string = "{0}".format(we.at[index, "username"])
                    printTitle(string)
                    horizontalSeperatorWeight(we.at[index, "male"])
                # print out next user
                if we.at[index, "male"]:
                    string = "| {} | {:.1f} kg | Neck: {:.1f} cm | Waist: {:.1f} cm | Bodyfat: {:.1f} % |".format(row["date"].strftime("%Y-%m-%d"), row["weight"], row["neck"], row["waist"], row["bf"])
                else:
                    string = "| {} | {:.1f} kg | Neck: {:.1f} cm | Waist: {:.1f} cm | Hip: {:.1f} cm | Bodyfat: {:.1f} % |".format(row["date"].strftime("%Y-%m-%d"), row["weight"], row["neck"], row["waist"], row["hip"], row["bf"])
                print(string)
                if index == len(we.index):
                    horizontalSeperatorWeight(we.at[index, "male"])
            print()
        ##################################################################################
        # works as expected
        elif option == 9:
            printTitle("Users")
            users = User.queryAll()
            for index, row in users.iterrows():
                string = ("| ID: {} | Name: {} | Birthday: {} | Male: {} | Height: {} cm |").format(index, row["name"], row["birthday"].strftime("%Y-%m-%d"), row["male"], row["height"])
                if index == 1:
                    horizontalSeperator(length =len(string)-2)
                print(string)
                horizontalSeperator(length =len(string)-2)
            print()
        ##################################################################################
        # works as expected
        elif option == 0:
            clear()
            break

####################################################################################
####################################################################################
####################################################################################
# show Menu for analysis
def analysisMenu():
    clear()
    print()
    while True:
        printTitle("Analysis Menu")
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
        printMenu(options)
        while True:
            option = input("Option: ")
            try:
                option = int(option)
                if option <= len(options["#"])-2 and option >= 0:
                    break
                else:
                    invalidInput()
            except ValueError:
                invalidInput()
        clear()
        print()
        if option == 1:
            printTitle("Show Mountain with Summits")
            #showMountainSummits(engine)
            #horizontalSeperator()
        elif option == 2:
            printTitle("Analysis for skitouring")
        elif option == 3:
            printTitle("Analysis for hiking")
        elif option == 4:
            printTitle("Analysis for running")
        elif option == 5:
            printTitle("Weight Analysis")
        elif option == 0:
            clear()
            break
