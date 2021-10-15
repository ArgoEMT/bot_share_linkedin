from api.user_api import *

def main () :
    me = get_me()
    print(me.firstName)
    print(me.lastName)
    print(me.id)

if __name__ == '__main__':
    main()
