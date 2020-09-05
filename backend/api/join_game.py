from flask import Blueprint, session, request

from backend.global_state import games

join_game = Blueprint('join_game', __name__)
@join_game.route('/join-game', methods=['POST'])
def join_game_controller():
    print("[API] join_game called")
    username = session["username"]
    request_body = request.get_json()
    game_id = request_body["gameId"]
    games[game_id].players.append(username)
    return { "players": games[game_id].players }