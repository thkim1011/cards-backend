from flask_socketio import leave_room, send

def create_exit_handler(socketio):
    @socketio.on('exit')
    def on_exit(data):
        username = data['username']
        id = data['id']
        leave_room(id)
        send(username + ' has left the room', room=id)
    return on_exit
