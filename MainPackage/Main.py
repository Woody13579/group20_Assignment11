# Main.py
import requests
import json
from FunctionsPackage.Functions import *

# https://api.nasa.gov

APIData = GrabAPIData('https://api.nasa.gov/neo/rest/v1/feed?start_date=2022-11-01&end_date=2022-11-08&api_key=fBoYX5TUzDqTxIRecScifonqnrIXs1wrXqF98D1R')
print(APIData)
