from classes.share import *
from helpers.get_header import *
import json
import requests
import sys
sys.path.insert(1, './')


def get_share(urn):
    response = requests.get(
        f"https://api.linkedin.com/v2/shares",
        params={'q': 'owners', 'owners': urn, 'sortBy': 'CREATED'},
        headers=get_header()
    )
    print(response.url)
    if (response.status_code != 200):
        print(f"Error : {response.content}")
        return None
    else:
        responseJson = json.loads(response.content)
        return Share.fromJson(responseJson)


get_share('54165')
