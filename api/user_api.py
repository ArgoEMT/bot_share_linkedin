import sys
sys.path.insert(1, './')
import requests
import json
from helpers.get_header import *
from classes.user import *


def get_me():
    response = requests.get(
        "https://api.linkedin.com/v2/me",
        headers=get_header()
    )
    if (response.status_code != 200):
        print(f"Error : {response.content}")
        return None
    else: 
        responseJson = json.loads(response.content)
        return User.fromJson(json=responseJson)