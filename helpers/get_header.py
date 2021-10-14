import json

def get_header():
    with open("credentials.json", "r") as jsonFile:
        new_credentials = json.load(jsonFile)
    return {'Authorization': 'Bearer ' + new_credentials["grant_token"]}