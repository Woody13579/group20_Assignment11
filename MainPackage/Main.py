# Main.py
import requests
import json
from FunctionsPackage.Functions import *

# https://api.nasa.gov
# we are using the NEO Asteroids - NeoWs data
# This is where we get out API data from.
APIData = GrabAPIData('https://api.nasa.gov/neo/rest/v1/feed?start_date=2022-11-01&end_date=2022-11-08&api_key=fBoYX5TUzDqTxIRecScifonqnrIXs1wrXqF98D1R')
# We want to only look at the Near Earth Objects data so we will now sepperate it
NEOData=APIData["near_earth_objects"]
Day='2022-11-02' # Change this to the day of the year you want information on
NEODay=NEOData[Day]
count=0
try:
    for asteroid in NEODay:
        AsteroidData=NEODay[count]
        print(AsteroidData['name'])
        count=count+1
    print("There were a total of "+str(count)+" asteroids near earth on "+Day+", all named above")
except:
    print("An error was made when attempting to show a list of the asteroid names. Please ensure the data format is ####-##-##")