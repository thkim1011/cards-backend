from flask import session
from flask_socketio import join_room, send

from backend.global_state import games

def create_join_handler(socketio):
    @socketio.on('join')
    def on_join(data):
        id = data['id']
        games[id].players.append(session['username'])
        join_room(id)
        username = session['username']
        send(username + ' has entered the room', room=id)
        print(username + ' has entered the room')
    return on_join