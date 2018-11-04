# classes
from classes import tb_country, session
#sqlalchemy
from classes import Column, String, Integer, Sequence
#sqlalchemy.ext.declarative
from classes import Base

# Class Definition
class Country(Base):
    __tablename__ = tb_country

    id = Column(Integer, Sequence('id'), primary_key=True)
    name = Column("name",String(80), nullable = False)
    code = Column("code",String(5), nullable = False)

    def __repr__(self):
        return "<Country (id = '%s', name='%s', countrycode='%s')>" % (self.id, self.name, self.code)
