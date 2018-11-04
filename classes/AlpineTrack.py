from classes import tb_tracksalpine, tb_sport, tb_mountains, tb_difficulty, session
#sqlalchemy
from classes import Column, Integer, Sequence, DateTime, Text, Boolean, Float, ForeignKey
#sqlalchemy.orm
from classes import relationship
#sqlalchemy.ext.declarative
from classes import Base

# Class Definition
class AlpineTrack(Base):
    __tablename__= tb_tracksalpine

    id = Column(Integer, Sequence('id'), primary_key=True)
    date_duration = Column('date_duration',DateTime, nullable = False)
    conditions = Column("conditions",Text)
    summit = Column("Including Summit",Boolean, nullable=False)
    distance = Column("distance", Float, nullable=False)
    ascend = Column("ascend", Integer, nullable = False)
    descend = Column("descend",Integer,nullable = False)

    mountain_id = Column(Integer, ForeignKey("%s.id" %(tb_mountains)))
    mountain = relationship("Mountain")

    sport_id = Column(Integer, ForeignKey("%s.id" %(tb_sport)))
    sport = relationship("Sport")

    difficulty_id = Column(Integer, ForeignKey("%s.id" %(tb_difficulty)))
    difficulty = relationship("Difficulty")

    def __repr__(self):
        return "<Mountains (id = '%s', name='%s', country='%s', mountainrange='%s', elevation='%s', mountaintype='%s')>" % (self.id, self.name, self.country.name, self.mrange, self.elevation, self.mtype.name)

    # new AlpineTrack
    @classmethod
    def new(self):
        print()
        newAT = AlpineTrack()
        # Ask for Date & Duration
        newAT.date_duration = DateDuration()
        horizontalSeperator()
        # Select mountain
        newAT.mountain_id = selectMountain(Engine)
        horizontalSeperator()
        # Enter if Summit was climbed or not
        while True:
            i = input("Does this include the summit? (Y/N)? ")
            if (i == "J" or i =="j" or i == "y" or i == "Y"):
                # Summit was climbed
                newAT.summit = True
                break
            elif (i == "N" or i == "n"):
                # Summit was NOT climbed
                newAT.summit = False
                break
            else:
                horizontalSeperator(string = "!")
                print("%s is an invalid Option. Try again!" % option)
        # Select Sport and Difficulty
        newAT.sport_id = selectSport()
        newAT.difficulty_id = selectDifficulty(sportID)
        horizontalSeperator()
        # Enter Conditions & Weather
        newAT.conditions = input("How were the conditions & weather? ")
        horizontalSeperator()
        # Enter Horizontal Distance
        newAT.distance = convertStringToFloat(input("Enter the horizontal distance in km: "))
        # Enter Meters of Ascend
        newAT.ascend = int(input("Enter vertical meters ascend: "))
        # Enter Meters of Descend
        newAT.descend = int(input("Enter vertical meters descend: "))
        # Print what was entered
        horizontalSeperator()
        print("New Alpine Tour:\n%s" %(newAT.name))
        # Ask if User wants to save new alpine track
        saveNewInput("Alpine Tour", newAT)

    def PerformanceSpeed(self):

        return ((self.ascend + self.descend)/100+self.distance)/(self.date_duration.hour + (self.date_duration.minute + (self.date_duration.second)/60)/60)
