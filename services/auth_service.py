import sys
sys.path.insert(1, './')
from api.auth_api import *
import json

with open("credentials.json", "r") as jsonFile:
    initial_credentials = json.load(jsonFile)

# auth_code = get_authorization_code(
#     client_id=initial_credentials["client_id"],
#     redirect_uri=initial_credentials["redirect_uri"],
# )


grant_token_response = get_grant_token(
    client_id=initial_credentials["client_id"],
    accessToken=initial_credentials["access_token"],
    client_secret=initial_credentials["client_secret"],
    redirect_uri=initial_credentials["redirect_uri"]
)
if(grant_token_response["status"] == 200):
    initial_credentials["grant_token"] = grant_token_response["content"]["access_token"]

    with open("credentials.json", "w") as jsonFile:
        json.dump(initial_credentials, jsonFile)

    with open("credentials.json", "r") as jsonFile:
        new_credentials = json.load(jsonFile)

else:
    print("Erreur de récupération du grant_token:")
    print(grant_token_response["content"])
