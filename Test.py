#!/usr/bin/python3.6

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

from classes import Base, Engine, Session, session
from sqlalchemy import *
from dbInterfacing import moveToDatabase


Sport.new()
newSport2 = Sport(name="Wandern")
