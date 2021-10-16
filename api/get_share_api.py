import sys
sys.path.insert(1, './')
from classes.share import *
from helpers.get_header import *
import json
import requests


def get_share(companyUrn: str) -> Share :
    response = requests.get(
        "https://api.linkedin.com/v2/shares",
        params={'q': 'owners', 'owners': companyUrn, 'sortBy': 'CREATED'},
        headers=get_header()
    )
    if (response.status_code != 200):
        print(f"Error : {response.content}")
        return None
    else:
        responseJson = json.loads(response.content)
        return Share.fromJson(responseJson)


