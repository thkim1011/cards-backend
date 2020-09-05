from flask import session
from flask_socketio import join_room, emit

from backend.global_state import games

def create_join_handler(socketio):
    @socketio.on('join')
    def on_join(game_id):
        game_state = games[game_id]
        username = session.get('username')
        if (len(game_state.players) < game_state.num_players):
            game_state.players.append(username)
        else:
            game_state.spectators.append(username)
        join_room(game_id)
        emit('chatHistory', game_state.messages)
        message = username + ' has entered the room'
        game_state.messages.append(message)
        emit('chat', message, room=game_id)
        emit('players', { "players": game_state.players, "owner": game_state.owner }, room=game_id)
        print('[Socket] ' + username + ' has entered the room')
    return on_join