from flask import session
from flask_socketio import socketio, emit

from backend.global_state import games

def create_chat_handler(socketio):
    @socketio.on('chat')
    def handle_chat(game_id, message):
        username = session['username']
        games[game_id].messages.append((username, message))       
        print('[Socket] ({0}) Received message \'{1}\' from {2}'.format(game_id, message, username))
        emit('chat', '{0}: {1}'.format(username, message), broadcast=True)
    return handle_chat