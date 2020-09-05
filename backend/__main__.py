from flask import Flask, session, render_template, request
from flask_socketio import SocketIO, join_room, leave_room, send
from flask_cors import CORS, cross_origin
from flask_session import Session

from backend.api.new_game import new_game
from backend.api.get_user_info import get_user_info
from backend.global_state import games

from backend.socket.join import create_join_handler
from backend.socket.exit import create_exit_handler
from backend.socket.message import create_message_handler

app = Flask(__name__)
# CORS
app.config['SECRET_KEY'] = 'secret!'
CORS(app, supports_credentials=True)

app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# SOCKET IO
socketio = SocketIO(app, cors_allowed_origins="*", manage_session=False)

on_join = create_join_handler(socketio)
on_exit = create_exit_handler(socketio)
message = create_message_handler(socketio)

# Blueprints
app.register_blueprint(new_game)
app.register_blueprint(get_user_info)

if __name__ == '__main__':
    socketio.run(app)
