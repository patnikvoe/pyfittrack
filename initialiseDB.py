#!/usr/bin/python3.6

# Import all classes
from classes.classes import *
from classes.functions import moveToDatabase
from classes import Base, Engine, session
from sqlalchemy import *

Base.metadata.create_all(Engine)
d= {"Sport": ["Skitour","Wandern", "Klettern", "Klettersteig", "Schneeschuhwanderung","Hochtour","Skihochtour","Trailrunning","Eisklettern"]}
df = pd.DataFrame(d)
df = df.sort_values(["Sport"], ascending=[True])
for index, row in df.iterrows():
    sport = Sport(name=row["Sport"])
    session.add(sport)

session.commit()

session.add_all([Difficulty(code="S1",description="Skitouren bis 30 Grad, dazu können noch Gipfelanstiege kommen, die Trittsicherheit und Schwindelfreiheit erfordern. Bei der Abfahrt: Erste Tiefschneekenntnisse. Sie fahren kontrolliert Kurven auf allen Pisten in paralleler Skistellung.",sport_id="7"),
Difficulty(code="S2",description="Skitouren bis 35 Grad, sicheres Beherrschen der Spitzkehrentechnik, Trittsicherheit und Schwindelfreiheit, eventuell braucht man die Hände fürs Gleichgewicht. Bei der Abfahrt: Sicheres Kurvenfahren im Tiefschnee auch im steileren und/oder unübersichtlichen Gelände in paralleler Skistellung, aus Sicherheitsgründen gelegentlich in der Spur des Fachübungsleiters.",sport_id="7"),
Difficulty(code="S3",description="Skitouren über 35 Grad, sehr sicheres Beherrschen der Spitzkehrentechnik, Trittsicherheit und Schwindelfreiheit, dazu können noch Kletterpassagen bis/über II. Schwierigkeitsgrad kommen. Bei der Abfahrt: Beherrschen des Kurvenfahrens in paralleler Skistellung im Tiefschnee bei allen Schneearten, auch im steilen und sehr steilen Gelände, auch mit höherem Tempo und unterschiedlichen Radien. Dies gilt ebenso bei Freeride Touren extrem steilen Gelände.",sport_id="7"),
Difficulty(code="W1",description="Wandern auf breiten Wegen und markierten Wanderpfaden, keine Absturzgefahr",sport_id="9"),
Difficulty(code="W2",description="Wandern auf markierten Wanderpfaden, exponierten Stellen möglich, die Trittsicherheit und Schwindelfreiheit erfordern",sport_id="9"),
Difficulty(code="W3",description="Wandern auf markierten Wanderpfaden, mit exponierten Stellen, die Trittsicherheit und Schwindelfreiheit erfordern, ausgesetzte Stellen können mit Seilen oder Ketten gesichert sein, eventuell braucht man die Hände fürs Gleichgewicht",sport_id="9"),
Difficulty(code="B1",description="Begehen von markierten Steigen, Geröllflächen, weglosen Schrofen, Gelände bereits recht exponiert, erfordert Trittsicherheit und Schwindelfreiheit sowie Alpinklettern I. Schwierigkeitsgrad",sport_id="9"),
Difficulty(code="B2",description="Begehen von markierten Steigen und weglosem Gelände, heikle Grashalden, steile Geröllflächen, einfache Firnfelder, erfordert Trittsicherheit und Schwindelfreiheit sowie Alpinklettern bis II. Schwierigkeitsgrad",sport_id="9"),
Difficulty(code="B3",description="Begehen von meist weglosem Gelände, steilen Schrofen, Firnfelder mit Ausrutschgefahr, erfordert Trittsicherheit und Schwindelfreiheit sowie Alpinklettern über II. Schwierigkeitsgrad",sport_id="9")
])

session.commit()

session.add_all([User(name="Patrick", birthday="1991-05-17", male = True, height=180),
User(name="Ania", birthday="1994-02-13", male = False, height = 158)])
session.commit()
session.add_all([
Weight(date = "2018-01-05",weight = 82.2, neck= 40.0, waist= 84.0, hip=0.0, user_id=1),
Weight(date = "2018-01-11",weight = 81.3, neck= 39.5, waist= 84.0, hip=0.0, user_id=1),
Weight(date = "2018-01-14",weight = 81.6, neck= 40.0, waist= 83.5, hip=0.0, user_id=1),
Weight(date = "2018-01-18",weight = 82.1, neck= 40.0, waist= 86.0, hip=0.0, user_id=1),
Weight(date = "2018-02-01",weight = 81.5, neck= 39.0, waist= 89.0, hip=0.0, user_id=1),
Weight(date = "2018-02-25",weight = 81.6, neck= 41.0, waist= 83.5, hip=0.0, user_id=1),
Weight(date = "2018-03-04",weight = 80.5, neck= 41.0, waist= 82.8, hip=0.0, user_id=1),
Weight(date = "2018-03-14",weight = 79.9, neck= 41.0, waist= 83.5, hip=0.0, user_id=1),
Weight(date = "2018-04-10",weight = 79.0, neck= 39.0, waist= 82.0, hip=0.0, user_id=1),
Weight(date = "2018-04-15",weight = 79.4, neck= 40.0, waist= 84.2, hip=0.0, user_id=1),
Weight(date = "2018-04-23",weight = 78.6, neck= 39.0, waist= 83.0, hip=0.0, user_id=1),
Weight(date = "2018-04-30",weight = 78.8, neck= 39.0, waist= 83.0, hip=0.0, user_id=1),
Weight(date = "2018-05-15",weight = 79.6, neck= 39.5, waist= 83.5, hip=0.0, user_id=1),
Weight(date = "2018-05-15",weight = 79.0, neck= 40.0, waist= 82.0, hip=0.0, user_id=1),
Weight(date = "2018-05-21",weight = 80.3, neck= 40.5, waist= 83.0, hip=0.0, user_id=1),
Weight(date = "2018-11-07",weight = 83.5, neck= 41.0, waist= 91.0, hip=0.0, user_id=1)])
session.commit()
session.add_all([
RouteRun(name="Friedhofsrunde",location="Rosenheim",distance = 1.85),
RouteRun(name="Kleine Mehlmühle",location="Dorfen",distance = 3.19),
RouteRun(name="Große Mehlmühle",location="Dorfen",distance = 3.84),
RouteRun(name="kleine Seerunde",location="Krakau",distance = 2.87),
RouteRun(name="Mangfall 6 Brücken",location="Rosenheim",distance = 6.95)])
session.commit()

session.add_all([
MountainType(name="Pass"),
MountainType(name="Gipfel"),
MountainType(name="Vulkan")])
session.commit()

#Countries
session.add_all([
Country(name="Polen", code="PL"),
Country(name="Deutschland", code="D"),
Country(name="Österreich", code="A"),
Country(name="Deutschland/Österreich", code="A/D")])
session.commit()

#Mountains
session.add_all([
Mountain(name="Turbacz", mrange="Karpaten - Gorce", elevation = 1310, mtype_id=2 , country_id=1),
Mountain(name="Kasprowy Wierch", mrange="Karpaten - Tatra", elevation = 1987, mtype_id=2 , country_id=1),
Mountain(name="Kampenwand", mrange="Chiemgauer Alpen", elevation = 1669, mtype_id=2 , country_id=2),
Mountain(name="Geigelstein", mrange="Chiemgauer Alpen", elevation = 1808, mtype_id=2 , country_id=2),
Mountain(name="Spitzstein", mrange="Chiemgauer Alpen", elevation = 1598, mtype_id=2 , country_id=4),
Mountain(name="Heuberg", mrange="Chiemgauer Alpen", elevation = 1338, mtype_id=2 , country_id=2),
Mountain(name="Karb", mrange="Karpaten - Tatra", elevation = 1853, mtype_id=1 , country_id=1)])

session.commit()
