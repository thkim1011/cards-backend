from flask import Blueprint, session, request
import random
import string

from backend.global_state import games
from backend.model.GameState import GameState

new_game = Blueprint('new_game', __name__)
@new_game.route('/new-game', methods=['POST'])
def new_game_controller():
    request_body = request.get_json()
    print('[API] Creating new game with game type {0} and num players {1}'\
        .format(request_body["gameType"], request_body["numPlayers"]))
    game_state = GameState(request_body["gameType"], request_body["numPlayers"])
    game_state.set_owner(session['username'])
    games[game_state.game_id] = game_state
    return { "gameId": game_state.game_id }