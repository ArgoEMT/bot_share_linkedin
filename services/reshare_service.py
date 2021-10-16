import sys
sys.path.insert(1, './')
import api.reshare_api as api
from classes.reshare import *

def post_reshare(reshare: Reshare) :
    body = reshare.toJson
    api.post_reshare(body = body)