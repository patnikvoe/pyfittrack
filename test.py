from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    addresses = relationship("Weight", backref="user")

class Weight(Base):
    __tablename__ = 'weight'
    id = Column(Integer, primary_key=True)
    weight = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
