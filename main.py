from flask import Flask
from flask_socketio import SocketIO, emit
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins = "*")

@app.route("/")
def hello():
    return "Hello, SmartNinja! SocketIO1"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
