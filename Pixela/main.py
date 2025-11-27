"""Habit Tracking"""

import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_TOKEN = "adkaufhafjnajvna"
PIXELA_USER = "ariff"
PIXELA_GRAPH_ID = "graphrun1"

PIXELA_USER_PARAM = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# TO CREATE PIXELA USER
# response = requests.post(PIXELA_ENDPOINT, json=PIXELA_USER_PARAM, timeout=1200)
# print(response.text)
# {"message":"Success. Let's visit https://pixe.la/@ariff , it is your profile page!","isSuccess":true}

# TO CREATE A GRAPH DEFINITION
PIXELA_GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USER}/graphs"
PIXELA_GRAPH_HEADER = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}
PIXELA_GRAPH_PARAM = {
    "id": "graphrun1",
    "name": "Graph_Run",
    "unit": "kilometer",
    "type": "float",
    "color": "momiji",
}

today = datetime.now()
today = today.strftime("%Y%m%d")

# response = requests.post(PIXELA_GRAPH_ENDPOINT, json=PIXELA_GRAPH_PARAM, headers=PIXELA_GRAPH_HEADER, timeout=1200)
# print(response.text)

# CREATE PIXEL TO THE GRAPH
PIXELA_VALUE_ENDPOINT = f"{PIXELA_GRAPH_ENDPOINT}/{PIXELA_GRAPH_ID}"
PIXELA_VALUE_PARAM = {
    "date": today,
    "quantity": input("How many kilometer did you run today?"),
}
# response = requests.post(PIXELA_VALUE_ENDPOINT, json=PIXELA_VALUE_PARAM , headers=PIXELA_GRAPH_HEADER, timeout=1200)
# print(response.text)
# {"message":"Success.","isSuccess":true}
# https://pixe.la/v1/users/ariff/graphs/graphrun1.html

# UPDATE PIXEL TO THE GRAPH
PIXELA_VALUE_UPDATE_ENDPOINT = f"{PIXELA_VALUE_ENDPOINT}/20251120"
PIXELA_VALUE_UPDATE_PARAM = {
    "quantity": "15.8",
}
# response = requests.put(PIXELA_VALUE_UPDATE_ENDPOINT, json=PIXELA_VALUE_UPDATE_PARAM, headers=PIXELA_GRAPH_HEADER, timeout=1200)
# print(response.text)
# {"message":"Success.","isSuccess":true}

# DELETE PIXEL TO THE GRAPH
# response = requests.delete(PIXELA_VALUE_UPDATE_ENDPOINT, headers=PIXELA_GRAPH_HEADER, timeout=1200)
# print(response.text) # {"message":"Success.","isSuccess":true}
