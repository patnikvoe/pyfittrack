#!/usr/bin/python3.6

# Import all classes
from classes.classes import *
from classes.functions import moveToDatabase
from classes import Base, Engine, session
from sqlalchemy import *

Base.metadata.create_all(Engine)


UID = 13

for user in session.query(User).filter(User.id==UID):
    pat = User(name=user.name,birthday=user.birthday,male =user.male,height=user.height)

# cancel = True
# while cancel:
#     i = input("Continue Input? (y/n)")
#
#     if i == "y" or i == "Y" or i =="j" or i== "J":
#         pat.newWeight()
#     else:
#         cancel = False




for weight in session.query(Weight).filter(Weight.user_id == UID):
    pat.weights.append(weight)


# Accessing all weights of User
for i in range(len(pat.weights)):
    print(pat.weights[i].weight)
    print(pat.weights[i].date)
