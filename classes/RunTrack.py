class RunTrack(Base):
    __tablename__='runtracks'
    id = Column(Integer, Sequence('id'), primary_key=True)
    date_duration = Column('date_duration',DateTime, nullable = False)
    route_id = Column(Integer, ForeignKey('routes.id'))
    route = relationship("Route")

    def pace(self):
        distance = float(self.route.distance)
        # Return pace in min/km
        return round((self.date_duration.hour*60 + self.date_duration.minute + self.date_duration.second/60) / distance,3)
    def speed(self):
        # Return Speed in km/h
        return round(60/self.pace(),2)

    def __repr__(self):
        return "<Running Track (id = '%s', date_duration='%s', pace='%s', speed='%s')>" % ( 
                    self.id, self.date_duration, self.pace(), self.speed())