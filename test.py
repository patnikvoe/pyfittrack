import matplotlib.pyplot as plt
import pandas as pd
import sqlalchemy
from tabulate import tabulate

#read whole table from DB
def readTableFromDB(db_table, db=engine, parse_dates=[], index_col="id", columns=None):
    return pd.read_sql_table(db_table,db,index_col = index_col, columns=columns,parse_dates=parse_dates)

# User Input date and duration
def DateDuration():
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
    #horizontalSeperator()
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


class RunTrack(Base):
    __tablename__='runtracks'
    id = Column(Integer, Sequence('id'), primary_key=True)
    date_duration = Column('date_duration',DateTime, nullable = False)
    route_id = Column(Integer, ForeignKey('routes.id'))
    route = relationship("Route")

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

class Route(Base):
    __tablename__ = "routes"

    id = Column(Integer, Sequence("id"), primary_key=True)
    name = Column("name",String(50), nullable=False)
    location = Column("location",String(30), nullable=False)
    distance = Column("distance",Float, nullable=False)

    def __repr__(self):
        return "<Running Route (id = '%s', name='%s', location='%s', distance='%s')>" % (
                    self.id, self.name, self.location, self.distance)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

route1 = Route(name="Friedhofsrunde", location="Rosenheim", distance=1.85)
route1
session.add(route1)
our_route= session.query(Route).filter_by(id = route1.id).first()
our_route


trackdate = DateDuration()
track1 = RunTrack(date_duration = trackdate, route_id = route1.id, route=route1)
track1
session.add(track1)
our_track = session.query(RunTrack).filter_by(id=track1.id).first()
our_track

route1 is our_route
track1 is our_track

session.commit()
