from classes import tb_weight, tb_users, session
#sqlalchemy
from classes import Column, Integer, Sequence, DateTime, Float, ForeignKey, Date
#sqlalchemy.orm
from classes import relationship
#sqlalchemy.ext.declarative
from classes import Base

# Class Definition
class Weight(Base):
    __tablename__ = tb_weight

    id = Column(Integer, Sequence("id"), primary_key=True)
    date = Column("date",Date, nullable=False)
    weight = Column("weight",Float, nullable=False)
    stomach = Column("stomach",Float)
    neck = Column("neck",Float, nullable = False)
    waist = Column("waist", Float)
    hip = Column("hip",Float)

    user_id = Column(Integer, ForeignKey("%s.id" %(tb_users)))
    user = relationship("User")

    def bodyfat(self):
        if user.male:
            return round(86.01*log10(self.stomach - self.neck)-70.041*log10(user.height)+30.3,4)
        else:
            return round(163.205*log10(self.waist+self.hip-self.neck)-97.684*log10(user.height)-78.387,4)


    @classmethod
    def new(self):
        pass

    def __repr__(self):
        return "<Weight (username='%s', date='%s', weight='%s', avgBodyfat='%s')>" % (
                    self.user.name, self.date, self.weight, self.bodyfaf())
