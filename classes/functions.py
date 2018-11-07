from classes import log10, pd, time, datetime, tabulate, platform, os

# Database connection
from classes import Base, Engine, Session, session

#################################################################################
# Clear depending on OS
if platform == "linux" or platform == "linux2" or platform == "darwin":
    # linux and mac
    clear = lambda: os.system("clear") #on Linux System
elif platform == "win32":
    # Windows...
    clear = lambda: os.system("cls") #on Windows System

#################################################################################
#calculate bodyfat for males in %
def bodyfatMale(waist, neck, height):
    bf = 495/(1.0324-0.19077*log10(waist-neck)+0.15456*log10(height))-450
    return round(bf,1)

#################################################################################
#calculate bodyfat for females in %
def bodyfatFemale(waist, neck, hip, height):
    bf = 495/(1.29579-0.35004*log10(waist+hip-neck)+0.22100*log10(height))-450
    return round(bf,1)

#################################################################################
# select Proper calculations based on user gender
def bodyfat(waist,neck,hip,height,male):
    if male:
        return bodyfatMale(waist, neck, height)
    else:
        return bodyfatFemale(waist, neck, hip, height)

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
    horizontalSeperator(string ="!")
    print("Invalid Input! Try again!")
    pass

#################################################################################
# Print menu function
def printMenu(dict):
    printPanda(dict, printIndex=False)
    pass

#################################################################################
# print Pandas
def printPanda(panda, header = "keys", format = "psql", printIndex = True):
    print(tabulate(panda, headers = header,tablefmt=format, showindex=printIndex))
    pass

#################################################################################
# print the title
def printTitle(title):
    string = "|  %s  |" % title
    horizontalSeperator(length = len(string)-2)
    print(string)
    horizontalSeperator(length = len(string)-2)
    pass
    
#################################################################################
# Horizontal Seperator
def horizontalSeperator(string = "-",length = 42):
    print("+" + (string*(length//len(string)+1))[:length] + "+")
    pass

#################################################################################
# Horizontal Seperator for show menu
def horizontalSeperatorWeight(male):
    if male:
        print("+------------+---------+---------------+----------------+-----------------+")
    else:
        print("+------------+---------+---------------+----------------+---------------+-----------------+")
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
