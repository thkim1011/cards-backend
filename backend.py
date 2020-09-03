from flask import Flask, render_template, request
from flask_socketio import SocketIO
from flask_cors import CORS, cross_origin
import coolname

app = Flask(__name__)
# CORS
app.config['SECRET_KEY'] = 'secret!'
CORS(app)

# SOCKET IO
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/test', methods=['POST'])
@cross_origin()
def test():
    content = request.get_json()
    print(content)

@app.route('/user-info', methods=['GET'])
@cross_origin()
def user_info():
    return coolname.generate_slug(3)

if __name__ == '__main__':
    socketio.run(app)
