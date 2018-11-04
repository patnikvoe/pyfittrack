from classes import tb_mtype, session
#sqlalchemy
from classes import Column, Integer, Sequence, String
#sqlalchemy.ext.declarative
from classes import Base

# Class Definition
class MountainType(Base):
    __tablename__= tb_mtype

    id = Column(Integer, Sequence('id'), primary_key=True)
    name = Column("name",String(50), nullable = False)

    def __repr__(self):
        return "<Mountain Type (id = '%s', name='%s')>" % (self.id, self.name)

    # new Mountain Type
    @classmethod
    def new (self):
        print()
        newType = MountainType()
        # Ask for Name of Route
        newType.name = input("Enter Type of Mountain: ")
        # Print what was entered
        horizontalSeperator()
        print("New Mountain Type:\n%s" %(newType.name))
        # Ask if User wants to save new Monutain Type
        saveNewInput("mountain type", newType)
