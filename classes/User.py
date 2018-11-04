from classes import tb_users, session
#sqlalchemy.dialects.postgresql DataTypes
from classes import Column, Integer, Sequence, Date, Boolean, Float, String
#sqlalchemy.ext.declarative
from classes import Base

# Class Definition
class User(Base):
    __tablename__ = tb_users

    id = Column(Integer, Sequence("id"), primary_key=True)
    username = Column("name",String(50), nullable=False)
    birthday = Column("birthday",Date, nullable=False)
    male = Column("male",Boolean,nullable=False)
    height = Column("height",Float, nullable=False)

    def __repr__(self):
        return "<User (id = '%s', name='%s', birthday='%s', male='%s', height ='%s')>" % (
                    self.id, self.name, self.birthday, self.male, self.height)
    # Calculate the current age
    def age(self):
        today = date.today()
        return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
