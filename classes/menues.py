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
            previousEntries = readTableFromDB(tb_tracksrun, parse_dates=["DateDuration"])
            previousEntries = previousEntries.sort_values(by=["date_duration"])
            printPanda(previousEntries[-5:])
            addTrack(True)
        elif option == 2:
            print("Add new alpine track")
            previousEntries = readTableFromDB(tb_tracksalpine,columns=["mountain_id", "sport_id", "date_duration", "summit","performancespeed"],parse_dates=["date_duration"])
            previousEntries = previousEntries.sort_values(by=["date_duration"])
            printPanda(previousEntries[-5:])
            addTrack(False)
        elif option == 3:
            print("Add new running route")
            printPanda(readTableFromDB(tb_runroutes))
            #addRouteRunning()
        elif option == 4:
            print("Add new goals")
            printPanda(readTableFromDB(tb_rungoals,parse_dates=["date"]))
        elif option == 5:
            print("Add new mountain")
            printPanda(readTableFromDB(tb_mountains))
            #addMountain()
        elif option == 6:
            print("Add new sport")
            printPanda(readTableFromDB(tb_sport))
            #addSport()
        elif option == 7:
            print("Add new difficulty")
            printPanda(readTableFromDB(tb_difficulty))
            #addDifficulty()
        elif option == 8:
            print("Add new weight")
            printPanda(readTableFromDB(tb_weight,parse_dates=["date"]))
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
            routes = routes.sort_values(by=["Location","Name"])
            routes = routes.reset_index(drop=True)
            array = ["+"*routes.Name.map(len).max(), "+"*(routes.Distance.astype(str).map(len).max() +3)]
            for index, row in routes.iterrows():
                # check if new Location started and print out the routes in that Location if so
                if index == 0:
                    printTitle("{}".format(routes.at[index, "Location"]))
                    horizontalSeperatorMulti(array)
                elif routes.at[index, "Location"] != routes.at[index-1,"Location"]:
                    horizontalSeperatorMulti(array)
                    printTitle("{}".format(routes.at[index, "Location"]))
                    horizontalSeperatorMulti(array)
                # print out route
                string = "| "
                for column in routes.columns:
                    if column == "Name":
                        add = routes.at[index,"Name"]
                        while len(add)< routes.Name.map(len).max():
                            add += " "
                        string += "{} | ".format(add)
                    elif column == "Distance":
                        add = str(routes.at[index,"Distance"])
                        while len(add)< routes.Distance.astype(str).map(len).max()-2:
                            add += " "
                        string += "{} km | ".format(add)
                print(string)
                if index == len(routes.index)-1:
                    horizontalSeperatorMulti(array)
            print()
        elif option == 3:
            printTitle("Alpine Tracks")
            tracks = AlpineTrack.queryAll()
            printPanda(tracks)
        ##################################################################################
        # works as expected
        elif option == 4:
            printTitle("Mountains")
            mountains = Mountain.queryAll()
            mountains = mountains.drop(["mtype_id", "country_id"], axis=1)
            mountains.columns = ["Name", "Range", "Elevation", "Type", "Country"]
            mountains = mountains.sort_values(by=["Range","Name"])
            array = ["+"*mountains.Name.map(len).max(), "+"*(mountains.Elevation.astype(str).map(len).max() +2), "+"*mountains.Type.map(len).max(), "+"*mountains.Country.map(len).max()]
            mountains = mountains.reset_index(drop=True)
            for index, row in mountains.iterrows():
                if index == 0:
                    printTitle("{}".format(mountains.at[index, "Range"]))
                    horizontalSeperatorMulti(array)
                elif mountains.at[index, "Range"] != mountains.at[index-1, "Range"]:
                    horizontalSeperatorMulti(array)
                    printTitle("{}".format(mountains.at[index, "Range"]))
                    horizontalSeperatorMulti(array)
                string = "| "
                for column in mountains.columns:
                    if column == "Name" or column =="Country" or column == "Type":
                        add = mountains.at[index,column]
                        while len(add)< mountains[column].map(len).max():
                            add += " "
                        string += "{} | ".format(add)
                    elif column == "Elevation":
                        add = str(mountains.at[index,"Elevation"])
                        while len(add)< mountains.Elevation.astype(str).map(len).max()-2:
                            add += " "
                        string += "{} m | ".format(add)
                print(string)
                if index == len(mountains.index)-1:
                    horizontalSeperatorMulti(array)
            print()
        ##################################################################################
        # works as expected
        elif option == 5:
            printTitle("Mountain Types")
            mtype = MountainType.queryAll()
            mtype = mtype.sort_values(by=["name"])
            mtype.columns = ["Type"]
            mtype = mtype.reset_index(drop=True)
            maxLength = mtype.Type.map(len).max()
            horizontalSeperator(length =maxLength+2)
            for index, row in mtype.iterrows():
                string = "%s" %row["Type"]
                while len(string) < maxLength:
                    string += " "
                string = "| %s |" %string
                print(string)
                if index == len(mtype.index)-1:
                    horizontalSeperator(length=len(string)-2)
            print()
        ##################################################################################
        # works as expected
        elif option == 6:
            printTitle("Sports")
            sports = Sport.queryAll()
            sports = sports.sort_values(by=["Sport"])
            sports = sports.reset_index(drop=True)
            maxLength = sports.Sport.map(len).max()
            array = ["+"*sports.Sport.map(len).max()]
            # print out route
            for index, row in sports.iterrows():
                if index == 0:
                    horizontalSeperatorMulti(array)
                add = sports.at[index,"Sport"]
                while len(add)< sports.Sport.map(len).max():
                    add += " "
                string = "| {} | ".format(add)
                print(string)
                if index ==len(sports.index)-1:
                    horizontalSeperatorMulti(array)
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
                string = "| %s | Code: %s | Description:"  %(row["sport_id"], row["code"])
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
            we = we.sort_values(["username","date"])
            for index, row in we.iterrows():
                # check if new User started and print out the Username if so
                if index == 1:
                    printTitle("{0}".format(we.at[index, "username"]))
                    string, array = stringArrayRowWeight(we.at[index, "male"], row)
                    horizontalSeperatorMulti(array)
                elif we.at[index, "username"] != we.at[index-1,"username"]:
                    string, array = stringArrayRowWeight(we.at[index-1, "male"], row)
                    horizontalSeperatorMulti(array)
                    printTitle("{0}".format(we.at[index, "username"]))
                    string, array = stringArrayRowWeight(we.at[index, "male"], row)
                    horizontalSeperatorMulti(array)
                # print out next user
                string, array = stringArrayRowWeight(we.at[index, "male"], row)
                print(string)
                if index == len(we.index):
                    horizontalSeperatorMulti(array)
            print()
        ##################################################################################
        # works as expected
        elif option == 9:
            printTitle("Users")
            users = User.queryAll()
            users = users.sort_values(["name"])
            maxNameLength = users.name.map(len).max()
            array = ["Name: " + "+"*users.name.map(len).max(), "Birthday: " + "+"*10, "Male: " + "+"*5, "Height: " +"+"*3 + " cm"]
            horizontalSeperatorMulti(array)
            for index, row in users.iterrows():
                string = ""
                for column in users.columns:
                    if users.columns.get_loc(column) == 0:
                        string += "| Name: {:<{length}} |".format(row["name"],length=maxNameLength)
                    elif users.columns.get_loc(column) == 1:
                        string += " Birthday: {} |".format(row["birthday"].strftime("%Y-%m-%d"))
                    elif users.columns.get_loc(column) == 2:
                        string += " Male: {: <5} |".format(str(row["male"]))
                    elif users.columns.get_loc(column) == 3:
                        string +=" Height: {} cm |".format(row["height"])
                print(string)
                if index == len(users.index)-1:
                    horizontalSeperatorMulti(array)
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
