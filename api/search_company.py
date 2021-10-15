import sys
sys.path.insert(1, './')
import requests
import json
from helpers.get_header import *
from classes.company import *

def get_companies():
    response = requests.get(
        "https://api.linkedin.com/v2/companySearch?q=search",
         params={
            'networkDegree': 'S',
        },
        headers=get_header()
    )
    if (response.status_code != 200):
        print(f"Error : {response.content}")
        return None
    else: 
        responseJson = json.loads(response.content)
        # TODO: retourne une entreprise
        return Company.fromJson(json=responseJson)

# TEST get_companies
get_companies()