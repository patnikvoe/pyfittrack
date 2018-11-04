from classes import tb_mtype, tb_country, tb_mountains, session
#sqlalchemy
from classes import Column, Integer, Sequence, ForeignKey, String
#sqlalchemy.orm
from classes import relationship
#sqlalchemy.ext.declarative
from classes import Base

# Class Definition
class Mountain(Base):
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

    # new Mountain
    @classmethod
    def new (self):
        print()
        newM = Mountain()
        # Ask for Name of Route
        newM.name = input("Enter Name of Summit: ")
        # Ask for Location
        newM.countrycode = input("Enter Countrycode: ")
        # Ask for distance of Route
        newM.mrange = input("Enter Mountainrange: ")
        # Ask for distance of Route
        newM.elevation = input("Enter Elevation: ")
        # Ask for distance of Route
        newM.mtype = input("Enter Mountaintype (Pass, Mountain, Vulcan): ")
        # Print what was entered
        horizontalSeperator()
        print("New Mountain:\n%s" %(newM.name))
        saveNewInput("mountain", newM)
