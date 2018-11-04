# dbInterfacing
from dbInterfacing import moveToDatabase
# classes variables
from classes import tb_sport
#sqlalchemy.dialects.postgresql DataTypes
from classes import Column, Integer, Sequence, String
#sqlalchemy.ext.declarative
from classes import Base

# Class Definition
class Sport(Base):
    __tablename__= tb_sport

    id = Column(Integer, Sequence('id'), primary_key=True)
    name = Column("Sport",String(30), nullable = False)

    def __repr__(self):
        return "New Sport:\n%s" %(self.name)

    # new Sport
    @classmethod
    def new (self):
        print()
        newSport = Sport()
        # Ask for Name of Sport
        newSport.name = input("Enter Name of Sport: ")
        # Print what was entered
        horizontalSeperator()
        print("New Sport:\n%s" %(newSport.name))
        # Ask if User wants to save new sport
        saveNewInput("sport", newSport)
