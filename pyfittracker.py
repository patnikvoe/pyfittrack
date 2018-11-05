#!/usr/bin/python3.6

from sys import platform
from menues import *
import pandas as pd
import os
from time import sleep
import matplotlib.pyplot as plt
import time
import datetime
from tabulate import tabulate
from sqlalchemy import *
# Import all classes
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
# Database connection
from classes import Base, Engine, Session, session

if platform == "linux" or platform == "linux2" or platform == "darwin":
    # linux and mac
    clear = lambda: os.system("clear") #on Linux System
elif platform == "win32":
    # Windows...
    clear = lambda: os.system("cls") #on Windows System

def main():
    #set Pandas max rows
    pd.options.display.max_rows = 999

    while True:
        menumain()

if __name__ == "__main__":
    main()
