from flask_socketio import send

def create_message_handler(socketio):
    @socketio.on('message')
    def handle_message(message):
        print('received messsage: ' + message)
        send(message, broadcast=True)
    return handle_message