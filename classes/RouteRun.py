from classes import tb_routes, session
#sqlalchemy.dialects.postgresql DataTypes
from classes import Column, Integer, Sequence, Float, String
#sqlalchemy.ext.declarative
from classes import Base

# Class Definition
class RouteRun(Base):
    __tablename__ = tb_routes

    id = Column(Integer, Sequence("id"), primary_key=True)
    name = Column("name",String(50), nullable=False)
    location = Column("location",String(30), nullable=False)
    distance = Column("distance",Float, nullable=False)

    def __repr__(self):
        return "<Running Route (id = '%s', name='%s', location='%s', distance='%s')>" % (
                    self.id, self.name, self.location, self.distance)

    # new Route for running
    @classmethod
    def new (self):
        print()
        newRoute = RouteRun()
        # Ask for Name of Route
        newRoute.name = input("Enter Name of Route: ")
        # Ask for Location
        newRoute.location = input("Enter Location: ")
        # Ask for distance of Route & convert distance to Float
        newRoute.distance = convertStringToFloat(input("Enter Distance of Route in km: "))
        # Print what was entered
        horizontalSeperator()
        print("New Route for Running:\n%s" %(newRoute.name))
        # Ask if User wants to save new route
        saveNewInput("Route for Running", newRoute)
