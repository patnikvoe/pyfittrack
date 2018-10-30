from Fitness import *

# Calculate Pace with distance and duration in min/km
def calculatePace(distance,duration):

    # Replace all , with . in distance
    # distance = distance.replace(",",".")
    # Convert to float
    distance = float(distance)

    # Return pace in min/km
    return round((duration.hour*60 + duration.minute + duration.second/60) / distance,3)

# Calculate Speed from Pace in km/h
def calculateSpeed(pace):
    
    # Return Speed in km/h
    return round(60/pace,2)

# Calculate the Performace Speeds with duration (ascend & descend), distance, ascend descend in Lkm/h
def calculatePerformanceSpeed(date_duration, distance, ascend, descend):
    return ((ascend + descend)/100+distance)/(date_duration.hour + (date_duration.minute + (date_duration.second)/60)/60)

# Convert an string to float
def convertStringToFloat(input):
    # Check if entered with Comma -> replace if so
    if input.find(",",0,len(input))>0:
        input = input.replace(",",".")
    # convert distance to float
    return float(input)