from services.get_share_service import *
from services.reshare_service import *
from services.search_company_service import *
import random
from datetime import datetime


def main () :
    dateNow = datetime.now()
    followed_companies = get_companies()
    
    isPostOk = False
    while not isPostOk :
        i = random.randint(0, len(followed_companies) - 1)
        
        company = followed_companies[i]
        company_share = get_share(company)
        shareDate = datetime.fromtimestamp(company_share.time)

        dayDifference = (dateNow - shareDate).days
        if dayDifference < 7 :
            isPostOk = True
            
    reshare = Reshare(company_share)
    post_reshare(reshare)             
        

    
if __name__ == '__main__':
    main()