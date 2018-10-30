from sqlalchemy import *
from sqlite3 import dbapi2 as sqlite
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime
import time
from math import log10

PATH_TO_DB = "C:/Dropbox/Gesundheit/App/CL/data/patfit.v2.db"
connection_string = "sqlite+pysqlite:///{path_to_db}".format(path_to_db=PATH_TO_DB)
engine = create_engine(connection_string, module=sqlite)

tb_sport = "sport"
tb_mountains = "mountains"
tb_routes = "routes"
tb_difficulty = "difficulty"
tb_tracksrun = "tracksrun"
tb_tracksalpine = "tracksalpine"
tb_rungoals = "rungoals"
tb_weight = "weight"
tb_mtype = "mtype"
tb_country = "country"
tb_users = "users"

Base = declarative_base()


class AlpineTracks(Base):
    __tablename__= tb_tracksalpine
   
    id = Column(Integer, Sequence('id'), primary_key=True)
    date_duration = Column('date_duration',DateTime, nullable = False)
    conditions = Column("conditions",Text)
    summit = Column("Including Summit",Boolean, nullable=False)
    distance = Column("distance", Float, nullable=False)
    ascend = Column("ascend", Integer, nullable = False)
    descend = Column("descend",Integer,nullable = False)
   
    mountain_id = Column(Integer, ForeignKey("%s.id" %(tb_mountains)))
    mountain = relationship("Mountains")

    sport_id = Column(Integer, ForeignKey("%s.id" %(tb_sport)))
    sport = relationship("Sports")

    difficulty_id = Column(Integer, ForeignKey("%s.id" %(tb_difficulty)))
    difficulty = relationship("Difficulties")

    def __repr__(self):
        return "<Mountains (id = '%s', name='%s', country='%s', mountainrange='%s', elevation='%s', mountaintype='%s')>" % ( 
                    self.id, self.name, self.country.name, self.mrange, self.elevation, self.mtype.name)
   
    def PerformanceSpeed(self):

        return ((self.ascend + self.descend)/100+self.distance)/(
                   self.date_duration.hour + (self.date_duration.minute + (self.date_duration.second)/60)/60)

class Mountains(Base):
    __tablename__= tb_mountains
   
    id = Column(Integer, Sequence('id'), primary_key=True)
    name = Column("name",String(80), nullable = False)
    mrange = Column("Mountainrange",String(50))
    elevation = Column("elevation", Integer, nullable=False)

    mtype_id = Column(Integer, ForeignKey("%s.id" %(tb_mtype)))
    mtype = relationship("MountainType")

    country_id = Column(Integer, ForeignKey("%s.id" %(tb_country)))
    country = relationship("Country")

    def __repr__(self):
        return "<Mountains (id = '%s', name='%s', country='%s', mountainrange='%s', elevation='%s', mountaintype='%s')>" % ( 
                    self.id, self.name, self.country.name, self.mrange, self.elevation, self.mtype.name)

class Country(Base):
    __tablename__ = tb_country

    id = Column(Integer, Sequence('id'), primary_key=True)
    name = Column("name",String(80), nullable = False)
    code = Column("code",String(5), nullable = False)
        
    def __repr__(self):
        return "<Country (id = '%s', name='%s', countrycode='%s')>" % ( 
                    self.id, self.name, self.code)

class MountainType(Base):
    __tablename__= tb_mtype
   
    id = Column(Integer, Sequence('id'), primary_key=True)
    name = Column("name",String(50), nullable = False)
   
    def __repr__(self):
        return "<Mountain Type (id = '%s', name='%s')>" % ( 
                    self.id, self.name)

class Sports(Base):
    __tablename__= tb_sport
    
    id = Column(Integer, Sequence('id'), primary_key=True)
    name = Column("Sport",String(30), nullable = False)

    def __repr__(self):
        return "<Sport (id = '%s', sport='%s')>" % ( 
                    self.id, self.name)

class Difficulties(Base):
    __tablename__= tb_difficulty
    
    id = Column(Integer, Sequence('id'), primary_key=True)
    code = Column("code", String(10), nullable=False)
    description = Column("description", Text)
    sport_id = Column(Integer, ForeignKey("%s.id" %(tb_sport)))
    sport = relationship("Sports")
    
    def __repr__(self):
        return "<Difficulty (id = '%s', code='%s', sport='%s', description='%s')>" % ( 
                    self.id, self.code, self.sport.name, self.description)

class RunTracks(Base):
    __tablename__=tb_tracksrun
    id = Column(Integer, Sequence('id'), primary_key=True)
    date_duration = Column('date_duration',DateTime, nullable = False)
    route_id = Column(Integer, ForeignKey("%s.id" %(tb_routes)))
    route = relationship("Routes")

    def pace(self):
        distance = float(self.route.distance)
        # Return pace in min/km
        return round((self.date_duration.hour*60 + self.date_duration.minute + self.date_duration.second/60) / distance,3)

    def speed(self):
        # Return Speed in km/h
        return round(60/self.pace(),2)

    def __repr__(self):
        return "<Running Track (id = '%s', date_duration='%s', pace='%s', speed='%s')>" % ( 
                    self.id, self.date_duration, self.pace(), self.speed())

class Routes(Base):
    __tablename__ = tb_routes

    id = Column(Integer, Sequence("id"), primary_key=True)
    name = Column("name",String(50), nullable=False)
    location = Column("location",String(30), nullable=False)
    distance = Column("distance",Float, nullable=False)

    def __repr__(self):
        return "<Running Route (id = '%s', name='%s', location='%s', distance='%s')>" % ( 
                    self.id, self.name, self.location, self.distance)

class Users(Base):
    __tablename__ = tb_users

    id = Column(Integer, Sequence("id"), primary_key=True)
    username = Column("name",String(50), nullable=False)
    birthday = Column("birthday",DateTime, nullable=False)
    male = Column("male",Boolean,nullable=False)
    height = Column("height",Float, nullable=False)
    
    def age(self):
        today = date.today()
        return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

    def __repr__(self):
        return "<Running Route (id = '%s', name='%s', location='%s', distance='%s')>" % ( 
                    self.id, self.name, self.location, self.distance)

class Weights(Base):
    __tablename__ = tb_weight

    id = Column(Integer, Sequence("id"), primary_key=True)
    date = Column("date",Date, nullable=False)
    weight = Column("weight",Float, nullable=False)
    stomach = Column("stomach",Float)
    neck = Column("neck",Float, nullable = False)
    waist = Column("waist", Float)
    hip = Column("hip",Float)
    skf_chest = Column("skfChest",Float)
    skf_abdomen = Column("skfAbdomen", Float)
    skf_thigh =  Column("skfThigh", Float)
    skf_triceps =  Column("skfTriceps", Float)
    skf_subscapular =  Column("skfSubscapular", Float)
    skf_suprailiac =  Column("skfSuprailiac", Float)
    skf_axilla =  Column("skfAxilla", Float)

    user_id = Column(Integer, ForeignKey("%s.id" %(tb_users)))
    user = relationship("Users")
        
    def bodyfat_navy(self):
        if user.male:
            return round(86.01*log10(self.stomach - self.neck)-70.041*log10(user.height)+30.3,4)   
        else:
            return round(163.205*log10(self.waist+self.hip-self.neck)-97.684*log10(user.height)-78.387,4)
    
    # Jackson-Pollock 7-Site
    def bodyfat_JP7(self):
        
        skinfold_sum = (skf_chest + 
                        skf_abdomen + 
                        skf_thigh + 
                        skf_triceps + 
                        skf_subscapular + 
                        skf_suprailiac + 
                        skf_axilla)        
        if user.male:
            return (495/(1.112-(0.00043499*skinfold_sum)+(0.00000055*skinfold_sum^2)-(0.00028826*user.age))-450)
        else:
            return (495/(1.097-(0.00046971*skinfold_sum)+(0.00000056*skinfold_sum^2)-(0.00012828*user.age))-450)

    # Jackson-Pollock 3-Site
    def bodyfat_JP3(self):
        
        skinfold_sum = (skf_chest + 
                            skf_abdomen + 
                            skf_thigh)        
        if user.male:
            return (495/(1.10938-(0.0008267*skinfold_sum)+(0.0000016*skinfold_sum^2)-(0.0002574*user.age)) -450)
        else:
            return (495/(1.089733-(0.0009245*skinfold_sum)+(0.0000025*skinfold_sum^2)-(0.0000979*user.age))-450)

    def bodyfat_avg(self):

        if (skf_chest != None and 
            skf_abdomen != None and
            skf_thigh != None and
            skf_triceps != None and
            skf_subscapular != None and
            skf_suprailiac != None and
            skf_axilla != None):

            return (bodyfat_JP3()+bodyfat_JP7()+bodyfat_navy())/3
        
        elif (skf_chest !=None and 
            skf_abdomen != None and
            skf_thigh != None):
            
            return (bodyfat_JP3()+bodyfat_navy())/3

        else:
            return (bodyfat_navy())
           
    def __repr__(self):
        return "<Weight (username='%s', date='%s', weight='%s', avgBodyfat='%s')>" % ( 
                    self.user.name, self.date, self.weight, self.bodyfat_avg())
