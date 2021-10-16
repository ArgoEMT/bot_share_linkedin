import sys
sys.path.insert(1, './')
import json

from classes.share import *
class Reshare () :
    share : Share

    def __init__ (self, share) :
        self.share = share

    def toJson (self) :
        with open("credentials.json", "r") as jsonFile:
            initial_credentials = json.load(jsonFile)
        
        orgaId = initial_credentials["orga_id"]
        returnJson = {
            "originalShare": f"urn:li:share:{self.share.id}",
            "owner": f"urn:li:organization:{orgaId}"
        }
        return returnJson

# TEST: class Reshare
# share = Share("1", "me", "3000000")
# reshare = Reshare(share)
# print(reshare.toJson())