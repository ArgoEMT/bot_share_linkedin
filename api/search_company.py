import sys
sys.path.insert(1, './')
from classes.company import *
from helpers.get_header import *
import json
import requests


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
        elementsJson = json.loads(responseJson["elements"])
        companies = []
        for element in elementsJson:
            companies.append(Company.fromJson(json=element))
        return companies


# TEST get_companies
get_companies()
