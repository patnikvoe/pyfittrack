class Route(Base):
    __tablename__ = "routes"

    id = Column(Integer, Sequence("id"), primary_key=True)
    name = Column("name",String(50), nullable=False)
    location = Column("location",String(30), nullable=False)
    distance = Column("distance",Float, nullable=False)

    def __repr__(self):
        return "<Running Route (id = '%s', name='%s', location='%s', distance='%s')>" % ( 
                    self.id, self.name, self.location, self.distance)