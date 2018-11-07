# class variables
## table names:
from classes import tb_users, tb_weight, tb_mtype, tb_sport, tb_mountains, tb_routes, tb_difficulty, tb_country, tb_tracksrun, tb_tracksalpine
## id sequence names:
from classes import user_id, sport_id, mountain_id, route_id, difficulty_id, trackrun_id, trackalpine_id, weight_id, mtype_id, country_id
## PostSQL DataTypes
from classes import Column, Integer, Sequence, Date, Boolean, Float, String, ForeignKey, DateTime, Text
## SQLAlchemy connection
from classes import Base, Engine, relationship, session
# functions
from classes.functions import *
# pandas, log10
from classes import pd, log10

####################################################################################
####################################################################################
####################################################################################
# Class Definition
class MountainType(Base):
    __tablename__= tb_mtype

    id = Column(Integer, Sequence(mtype_id), primary_key=True)
    name = Column("name",String(50), nullable = False)

    # self representation
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

    # Query for all and return as panda
    @classmethod
    def queryAll(self):
        return readTableFromDB(tb_mtype,Engine)

    # selecting a Sport from the list in postgreSQL
    @classmethod
    def select(self):
        mtype = readTableFromDB(tb_mtype,Engine)
        print(tabulate(routes_in,headers = "keys",tablefmt="psql"))
        while True:
            selection = input("Select Mountain Type: ")
            selection = int(selection)
            if selection in mtype:
                break
            else:
                invalidInput()
        return selection

####################################################################################
####################################################################################
####################################################################################
# Class Definition
class Sport(Base):
    __tablename__= tb_sport

    id = Column(Integer, Sequence(sport_id), primary_key=True)
    name = Column("Sport",String(30), nullable = False)

    # self representation
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

    # Query for all and return as panda
    @classmethod
    def queryAll(self):
        return readTableFromDB(tb_sport,Engine)

    # selecting a Sport from the list in postgreSQL
    @classmethod
    def select(self):
        print(tabulate(sports,headers = "keys",tablefmt="psql"))
        while True:
            selection = input("Select Sport: ")
            selection = int(selection)
            if selection in sports:
                break
            else:
                invalidInput()
        return selection

    # selecting a Sport from the list in postgreSQL
    @classmethod
    def selectName(self, ID):
        selection = readTableFromDB(tb_sport,Engine)
        selection = selection.iloc[ID-1]
        selection = selection['Sport']
        return selection
####################################################################################
####################################################################################
####################################################################################
# Class Definition
class AlpineTrack(Base):
    __tablename__= tb_tracksalpine

    id = Column(Integer, Sequence(trackalpine_id), primary_key=True)
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

    # self representation
    def __repr__(self):
        return "<Mountains (id = '%s', name='%s', country='%s', mountainrange='%s', elevation='%s', mountaintype='%s')>" % (self.id, self.name, self.country.name, self.mrange, self.elevation, self.mtype.name)

    # Query for all and return as panda
    @classmethod
    def queryAll(self):
        return readTableFromDB(tb_tracksalpine,Engine)

    # new AlpineTrack
    @classmethod
    def new(self):
        print()
        newAT = AlpineTrack()
        # Ask for Date & Duration
        newAT.date_duration = enterDateDuration()
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

####################################################################################
####################################################################################
####################################################################################
# Class Definition
class Difficulty(Base):
    __tablename__= tb_difficulty

    id = Column(Integer, Sequence(difficulty_id), primary_key=True)
    code = Column("code", String(10), nullable=False)
    description = Column("description", Text)
    sport_id = Column(Integer, ForeignKey("%s.id" %(tb_sport)))

    sport = relationship("Sport")

    # self representation
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

    # Query for all and return as panda
    @classmethod
    def queryAll(self):
        return pd.read_sql_table(tb_difficulty,Engine, index_col="id")

    # Query for all and return as panda
    @classmethod
    def select(sport, self):
        # Query from postgreSQL
        dificulties = pd.read_sql_table(tb_difficulty,Engine, index_col="id")
        # Panda comperision
        difficultyBool = difficulty["sport_id"] == sport
        difficulty = difficulty[difficultyBool]
        #print dificulties for Sport
        print(tabulate(difficulty,headers = "keys",tablefmt="psql"))
        #Ask for intput
        selection = input("Select difficulty: ")
        selection = int(selection)
        return selection

####################################################################################
####################################################################################
####################################################################################
# Class Definition
class Country(Base):
    __tablename__ = tb_country

    id = Column(Integer, Sequence(country_id), primary_key=True)
    name = Column("name",String(80), nullable = False)
    code = Column("code",String(5), nullable = False)

    # self representation
    def __repr__(self):
        return "<Country (id = '%s', name='%s', countrycode='%s')>" % (self.id, self.name, self.code)

    # Query for all and return as panda
    @classmethod
    def queryAll(self):
        return readTableFromDB(tb_country
        ,Engine)

####################################################################################
####################################################################################
####################################################################################
# Class Definition
class Mountain(Base):
    __tablename__= tb_mountains

    id = Column(Integer, Sequence(mountain_id), primary_key=True)
    name = Column("name",String(80), nullable = False)
    mrange = Column("Mountainrange",String(50))
    elevation = Column("elevation", Integer, nullable=False)

    mtype_id = Column(Integer, ForeignKey("%s.id" %(tb_mtype)))
    mtype = relationship("MountainType")

    country_id = Column(Integer, ForeignKey("%s.id" %(tb_country)))
    country = relationship("Country")

    # self representation
    def __repr__(self):
        return "<Mountains (id = '%s', name='%s', country='%s', mountainrange='%s', elevation='%s', mountaintype='%s')>" % (
                    self.id, self.name, self.country.name, self.mrange, self.elevation, self.mtype.name)

    # Query for all and return as panda
    @classmethod
    def queryAll(self):
        return readTableFromDB(tb_mountains,Engine)

    # new Mountain
    @classmethod
    def new (self):
        print()
        newM = Mountain()
        # Ask for Name of Route
        newM.name = input("Enter Name of Summit: ")
        # Ask for Location
        newM.countrycode = input("Enter Countrycode: ")
        # Ask for distance of Route
        newM.mrange = input("Enter Mountainrange: ")
        # Ask for distance of Route
        newM.elevation = input("Enter Elevation: ")
        # Ask for distance of Route
        newM.mtype = input("Enter Mountaintype (Pass, Mountain, Vulcan): ")
        # Print what was entered
        horizontalSeperator()
        print("New Mountain:\n%s" %(newM.name))
        saveNewInput("mountain", newM)

####################################################################################
####################################################################################
####################################################################################
# Class Definition: TRACKRUN
class TrackRun(Base):
    __tablename__ = tb_tracksrun
    id = Column(Integer, Sequence(trackrun_id), primary_key=True)
    date_duration = Column('date_duration',DateTime, nullable = False)
    route_id = Column(Integer, ForeignKey("%s.id" %(tb_routes)))
    route = relationship("RouteRun")

    # self representation
    def __repr__(self):
        return "<Running Track (id = '%s', date_duration='%s', pace='%s', speed='%s')>" % (self.id, self.date_duration, self.pace(), self.speed())

    # Query for all and return as panda
    @classmethod
    def queryAll(self):
        return readTableFromDB(tb_tracksrun,Engine)

    # Calculate pace
    def pace(self):
        distance = float(self.route.distance)
        # Return pace in min/km
        return round((self.date_duration.hour*60 + self.date_duration.minute + self.date_duration.second/60) / distance,3)

    # Calculate speed
    def speed(self):
        # Return Speed in km/h
        return round(60/self.pace(),2)

    @classmethod
    def new(self):
        newT = TrackRun()
        # Ask for Date
        newT.date_duration = enterDateDuration()
        # Ask for route
        newT.route_id = RouteRun.select()
        # Print what was entered
        horizontalSeperator()
        print("New Track for Running:\n%s" %(newT.name, newT.date_duration, newT.route_id))
        # Ask if User wants to save new running track
        saveNewInput("Track for Running", newT)

####################################################################################
####################################################################################
####################################################################################
# Class Definition: USER
class User(Base):
    __tablename__ = tb_users

    id = Column(Integer, Sequence(user_id), primary_key=True)
    name = Column("name",String(50), nullable=False)
    birthday = Column("birthday",Date, nullable=False)
    male = Column("male",Boolean,nullable=False)
    height = Column("height",Integer, nullable=False) # in cm

    weights= relationship("Weight", back_populates="user")

    # self representation
    def __repr__(self):
        return "New User:\nName: %s\nBirthday: %s\nMale: %s\nHeight: %s" %(self.name, self.birthday, self.male, self.height)

    # Query for all and return as panda
    @classmethod
    def queryAll(self):
        return readTableFromDB(tb_users,Engine, parse_dates="birthday")

    # Add new user
    @classmethod
    def new (self):
        print()
        newU = User()
        # Ask for Name of User
        newU.name = input("Enter Name of User: ")
        # Ask for birthday of user
        print("Birthday of user %s: "%(newU.name))
        newU.birthday = enterDate()
        # Ask for male or female
        while True:
            i = input("Is the user female or male? (f/m): ")
            if i=="f" or i=="F":
                newU.male = False
                break
            elif i=="m" or i == "M":
                newU.male = True
                break
            else:
                print("Invalid Input! Try again!")
        # Ask for heigt of user
        newU.height = int(input("Enter height of user %s (in cm): " %(newU.name)))
        # Print what was entered
        horizontalSeperator()
        print("New User:\nName: %s\nBirthday: %s\nMale: %s\nHeight: %s cm" %(newU.name, newU.birthday, newU.male,newU.height))
        # Ask to save or delete
        saveNewInput("User", newU)
        pass

    # selecting a User from the list in postgreSQL
    @classmethod
    def select(self):
        users = readTableFromDB(tb_users,Engine, parse_dates="birthday")
        print(tabulate(users,headers = "keys",tablefmt="psql"))
        while True:
            selection = int(input("Select User: "))
            if selection > 0:
                try:
                    users.iloc[selection-1]
                except IndexError:
                    invalidInput()
                else:
                    break
            elif selection == 0:
                invalidInput()
        return selection

    # is User male or female?
    @classmethod
    def isMale(UID):
        for user in session.query(User).filter(User.id==UID):
            pat = User(name=user.name,birthday=user.birthday,male =user.male, height=user.height)
        return pat.male

    # how tall is user UID
    @classmethod
    def Height(UID):
        for user in session.query(User).filter(User.id==UID):
            pat = User(name=user.name,birthday=user.birthday,male =user.male, height=user.height)
        return pat.height

    # Calculate the current age of User
    def age(self):
        today = date.today()
        return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

    # Add new weight
    def newWeight (self):
        print()
        newW = Weight()
        # Ask for Name of User
        newW.user_id = self.id
        # Ask for date
        newW.date = enterDate()
        # Ask for user weight
        newW.weight = convertStringToFloat(input("Enter weight (in kg): "))
        # Ask for neck circumference
        newW.neck = convertStringToFloat(input("Enter neck circumference (in cm): "))
        # Ask for waist circumference
        newW.waist = convertStringToFloat(input("Enter waist circumference (in cm): "))
        # Ask for hip circumference
        ## Check if user is male or female

        if self.male == False:
            newW.hip = convertStringToFloat(input("Enter hip circumference (in cm): "))
        else:
            newW.hip = 0

        # Print what was entered
        horizontalSeperator()
        if self.male == True:
            print("New Measurements:\nuserID: %s\nDate: %s\nWeight: %.1f kg\nneck: %.1f cm\nwaist: %.1f cm" %(newW.user_id,
                newW.date, newW.weight,newW.neck, newW.waist))
        else:
            print("New Measurements:\nUserID: %s\nDate: %s\nWeight: %.1f kg\nNeck: %.1f cm\nWaist: %.1f cm\nHip: %.1f cm" %(newW.user_id,
                newW.date, newW.weight,newW.neck, newW.waist, newW.hip))
        # Ask to save or delete
        while True:
            i = input("Do you want to save the new measurements (Y/N)? ")
            if i == "J" or i =="j" or i == "y" or i == "Y":
                self.weights.append(newW)
                moveToDatabase(self)
                break
            elif i=="n" or i=="N":
                break
            else:
                print("Invalid Input! Try again!")
            pass
        pass

####################################################################################
####################################################################################
####################################################################################
# Class Definition
class Weight(Base):
    __tablename__ = tb_weight

    id = Column(Integer, Sequence(weight_id), primary_key=True)
    date = Column("date",Date, nullable=False)
    weight = Column("weight",Float, nullable=False) # in kg
    neck = Column("neck",Float, nullable = False) # in cm
    waist = Column("waist", Float) # in cm
    hip = Column("hip",Float) # in cm

    user_id = Column(Integer, ForeignKey("%s.id" %(tb_users)))
    user = relationship("User",back_populates="weights")

    # self representation
    def __repr__(self):
        return "<Weight (username='%s', date='%s', weight='%s', avgBodyfat='%.1f')>" % (
                    self.user.name, self.date, self.weight, self.bodyfat())

    # Query for all and return as panda
    @classmethod
    def queryAll(self):
        # create empty Dataframe
        d = pd.DataFrame(columns=["date", "weight", "waist", "neck", "hip", "bf", "male", "height", "user_id"])
        users = pd.DataFrame()
        # Append postgreSQL Table
        d = d.append(readTableFromDB(tb_weight,Engine), sort = False)
        users = users.append(readTableFromDB(tb_users,Engine), sort = False)
        # extract user height, male
        height = users.height.to_dict()
        male = users.male.to_dict()
        d["male"] = d.user_id.map(male)
        d["height"] = d.user_id.map(height)

        # iterate through DataFrame
        for index, row in d.iterrows():
            bodyf = bodyfat(row['waist'],row['neck'],row['hip'],row['height'],row['male'])
            d.at[index, "bf"] = bodyf

        return d



####################################################################################
####################################################################################
####################################################################################
# Class Definition
class RouteRun(Base):
    __tablename__ = tb_routes

    id = Column(Integer, Sequence(route_id), primary_key=True)
    name = Column("name",String(50), nullable=False)
    location = Column("location",String(30), nullable=False)
    distance = Column("distance",Float, nullable=False)


    # self representation
    def __repr__(self):
        return "New Route for Running:\n%s\n%s\n%.2f" %(newR.name,newR.location, newR.distance)

    # Query for all and return as panda
    @classmethod
    def queryAll(self):
        return readTableFromDB(tb_routes,Engine)

    # new Route for running
    @classmethod
    def new (self):
        print()
        newR = RouteRun()
        # Ask for Name of Route
        newR.name = input("Enter Name of Route: ")
        # Ask for Location
        newR.location = input("Enter Location: ")
        # Ask for distance of Route & convert distance to Float
        newR.distance = convertStringToFloat(input("Enter Distance of Route in km: "))
        # Print what was entered
        horizontalSeperator()
        print("New Route for Running:\n%s\n%s\n%.2f" %(newR.name,newR.location, newR.distance))
        # Ask if User wants to save new route
        saveNewInput("Route for Running", newR)

    # selecting a Sport from the list in postgreSQL
    @classmethod
    def select(self):
        routes = readTableFromDB(tb_routes,Engine)
        print(tabulate(routes,headers = "keys",tablefmt="psql"))
        while True:
            selection = input("Select Route: ")
            selection = int(selection)
            if selection in sports:
                break
            else:
                invalidInput()
        return selection
