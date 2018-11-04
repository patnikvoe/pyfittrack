from main import *

# Convert an string to float
def convertStringToFloat(input):
    # Check if entered with Comma -> replace if so
    if input.find(",",0,len(input))>0:
        input = input.replace(",",".")
    # convert distance to float
    return float(input)
