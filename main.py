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
from classes.AlpineTrack import AlpineTrack
from classes.Country import Country
from classes.Difficulty import Difficulty
from classes.Mountain import Mountain
from classes.MountainType import MountainType
from classes.RouteRun import RouteRun
from classes.Sport import Sport
from classes.TrackRun import TrackRun
from classes.User import User
from classes.Weight import Weight
# Database connection
from classes import Base, Engine, Session, session


def main():
    #set Pandas max rows
    pd.options.display.max_rows = 999

    while True:
        menumain()

if __name__ == "__main__":
    main()
