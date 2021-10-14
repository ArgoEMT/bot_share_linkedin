from api.user_api import *

me = get_me()
print(me.firstName)
print(me.lastName)
print(me.id)
