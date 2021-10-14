import requests
import json
from helpers.get_header import *
from classes.user import *


def get_me():
    response = requests.get(
        "https://api.linkedin.com/v2/me",
        headers=get_header()
    )

    return User.fromJson(json=json.loads(response.content))
