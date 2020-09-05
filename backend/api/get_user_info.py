from flask import Blueprint, session
import coolname

get_user_info = Blueprint('get_user_info', __name__)
@get_user_info.route('/get-user-info', methods=['GET'])
def get_user_info_controller():
    print("[API] get_user_info called")
    if not 'username' in session:
        session['username'] = coolname.generate_slug(3)
    return { "username": session['username'] }