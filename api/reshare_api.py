import sys
sys.path.insert(1, './')
import requests
from classes.reshare import *
from helpers.get_header import *


def post_reshare (body: dict[str, str]) :
    response = requests.post(
        url="https://api.linkedin.com/v2/shares",
        data = body,
        headers = get_header()
    )
    
    if(response.status_code != 200):
        print(f"Error : {response.content}")
        return None
    else :
        print('Success reposting')
        return