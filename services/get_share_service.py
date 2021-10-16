import sys
sys.path.insert(1, './')
import api.get_share_api as api
from classes.company import *
from classes.share import *

def get_share(company: Company) -> Share :
    urn = company.urn
    return api.get_share(companyUrn= urn)