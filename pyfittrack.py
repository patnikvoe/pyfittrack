#!/usr/bin/python3.6

# import required modules from classes
from classes import pd

#import Menues
from classes.menues import menumain, addMenu, showTablesMenu, analysisMenu

# Import all classes
from classes.classes import AlpineTrack, Country, Difficulty, Mountain, MountainType, RouteRun, Sport, TrackRun, User, Weight

# Database connection
from classes import Base, Engine, Session, session
from classes.functions import clear

# create Database if necessary
Base.metadata.create_all(Engine)

def main():
    #set Pandas max rows
    pd.options.display.max_rows = 999

    while True:
        menumain()

if __name__ == "__main__":
    main()
