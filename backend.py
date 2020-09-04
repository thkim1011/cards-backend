from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room, leave_room, send
from flask_cors import CORS, cross_origin
import coolname
import random
import string

app = Flask(__name__)
# CORS
app.config['SECRET_KEY'] = 'secret!'
CORS(app)

# games
games = {}

# SOCKET IO
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/newGame', methods=['POST'])
@cross_origin()
def newGame():
    content = request.get_json()
    id = ''.join(random.choice(string.ascii_uppercase) for i in range(10))
    games[id] = { "players" : [] }
    return id

@app.route('/user-info', methods=['GET'])
@cross_origin()
def user_info():
    return coolname.generate_slug(3)

@socketio.on('join')
def on_join(data):
    username = data['username']
    id = data['id']
    games[id]["players"].append(username)
    join_room(id)
    send(username + ' has entered the room', room=id)
    print(username + ' has entered the room')

@socketio.on('exit')
def on_exit(data):
    username = data['username']
    id = room['id']
    leave_room(id)
    send(username + ' has left the room', room=id)

@socketio.on('message')
def handle_message(message):
    print('received messsage: ' + message)
    send(message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
