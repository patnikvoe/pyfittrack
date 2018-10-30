from sys import platform
from menues import *
import pandas as pd
import os
from time import sleep
from sqlalchemy import Table, Column, Boolean, Integer, String, Text, Time, Float, MetaData, Date, ForeignKey, create_engine, DateTime
from sqlite3 import dbapi2 as sqlite
import matplotlib.pyplot as plt
import pandas as pd
import time
import datetime
from tabulate import tabulate


def main():
    tb_sport = "sport"
    tb_mountains = "mountains"
    tb_runroutes = "runroutes"
    tb_difficulty = "difficulty"
    tb_tracksrun = "tracksrun"
    tb_tracksalpine = "tracksalpine"
    tb_rungoals = "rungoals"
    tb_weight = "weight"

    #create connection to DB
    pd.options.display.max_rows = 999
    PATH_TO_DB = "C:/Dropbox/Gesundheit/App/CL/data/patfit.db"
    connection_string = "sqlite+pysqlite:///{path_to_db}".format(path_to_db=PATH_TO_DB)
    engine = create_engine(connection_string, module=sqlite)



    while True:
        menumain()

if __name__ == "__main__":
    main()


