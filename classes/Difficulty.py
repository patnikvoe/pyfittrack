from classes import tb_sport, tb_difficulty, session
#sqlalchemy
from classes import Column, Integer, Sequence, Text, ForeignKey, String
#sqlalchemy.orm
from classes import relationship
#sqlalchemy.ext.declarative
from classes import Base

# Class Definition
class Difficulty(Base):
    __tablename__= tb_difficulty

    id = Column(Integer, Sequence('id'), primary_key=True)
    code = Column("code", String(10), nullable=False)
    description = Column("description", Text)
    sport_id = Column(Integer, ForeignKey("%s.id" %(tb_sport)))
    sport = relationship("Sport")

    def __repr__(self):
        return "<Difficulty (id = '%s', code='%s', sport='%s', description='%s')>" % (
                    self.id, self.code, self.sport.name, self.description)
    # new Difficulty
    @classmethod
    def new():
        print()
        newD = Difficulty()
        # Ask for SportID
        newD.sport_id = selectSport()
        # Ask for difficulty code
        newD.code = input("Enter Difficulty Code: ")
        # Ask for description
        newD.description = input("Enter Description: ")
        # Print what was entered
        horizontalSeperator()
        print("New Sport:\n%s" %(newD.name))
        # Ask if User wants to save new sport
        saveNewInput("sport", newD)
