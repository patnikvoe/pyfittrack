from classes import tb_tracksrun, tb_routes, session
#sqlalchemy
from classes import Column, Integer, Sequence, DateTime, ForeignKey
#sqlalchemy.orm
from classes import relationship
#sqlalchemy.ext.declarative
from classes import Base

# Class Definition
class TrackRun(Base):
    __tablename__=tb_tracksrun
    id = Column(Integer, Sequence('id'), primary_key=True)
    date_duration = Column('date_duration',DateTime, nullable = False)
    route_id = Column(Integer, ForeignKey("%s.id" %(tb_routes)))
    route = relationship("RouteRun")

    def __repr__(self):
        return "<Running Track (id = '%s', date_duration='%s', pace='%s', speed='%s')>" % (self.id, self.date_duration, self.pace(), self.speed())

    def pace(self):
        distance = float(self.route.distance)
        # Return pace in min/km
        return round((self.date_duration.hour*60 + self.date_duration.minute + self.date_duration.second/60) / distance,3)

    def speed(self):
        # Return Speed in km/h
        return round(60/self.pace(),2)

    @classmethod
    def new(self):
        newTrack = TrackRun()
        # Ask for Date
        newTrack.date_duration = DateDuration()
        # Ask for route
        routes = readTableFromDB(tb_runroutes,Engine,parse_dates=[])
        newTrack.route_id, distance = selectRoute(routes)
        # Print what was entered
        horizontalSeperator()
        print("New Track for Running:\n%s" %(newTrack.name))
        # Ask if User wants to save new running track
        saveNewInput("Track for Running", newTrack)
