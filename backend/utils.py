from flask import session

def get_username():
    try:
        return session['username']
    except:
        raise Exception('get_user_info has not been called yet')