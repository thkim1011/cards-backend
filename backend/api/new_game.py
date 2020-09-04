from flask import Blueprint, session, request
import random
import string

from backend.global_state import games
from backend.model.GameState import GameState

new_game = Blueprint('new_game', __name__)
@new_game.route('/new-game', methods=['POST'])
def new_game_controller():
    request_body = request.get_json()
    print(request_body)
    game_state = GameState(request_body["gameType"])
    games[game_state.gameId] = game_state
    return { "gameId": game_state.gameId }