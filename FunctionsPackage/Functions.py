# Functions.py
import requests
import json

# This function will format a provided API 
def GrabAPIData(x):
    response = requests.get(x)
    json_string = response.content
    
    parsed_json = json.loads(json_string) # Now we have a python dictionary
    return parsed_json