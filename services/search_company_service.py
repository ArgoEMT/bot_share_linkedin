import sys
sys.path.insert(1, './')
import api.search_company_api as api
from classes.company import *

def get_companies() -> list[Company] :
    return api.get_companies()