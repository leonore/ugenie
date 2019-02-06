from flask import Flask, render_template, request
from flask_socketio import SocketIO

from model import agent

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#' # Secret key for encryption
socketio = SocketIO(app) # Apply SocketIO to 'app' to use it instead of app for running the application

sessionIds = [] # Collect connected Session IDs

# When the user enters the homepage ('/') it triggers the sessions view
@app.route('/')
def sessions():
        return render_template('session.html') # Helps render the HTML page, called a 'template'

def messageReceived(sessionId, message):
        print('Message received from', sessionID,': ', message)

def sendMessage(sessionId, message):
        print('Sending message!')
        json = {'user_name' : 'GUVA', 'message' : message}
        socketio.emit('print message', json)

@socketio.on('connect')
def handle_connection():
        # Get the session ID this event is associated with
        sessionId = request.sid
        
        # Print the welcome message on the chat interface
        sendMessage(sessionId, "Hello, I'm GUVA, the Glasgow University Virtual Assistant. How can I help you?")
        
@socketio.on('message')
def handle_message(json, methods=['GET', 'POST']):
        print('Received event: ' + str(json))

        # Get the session ID this event is associated with
        sessionId = request.sid
        
        # Print the message that was sent
        socketio.emit('print message', json)    # On the chat interface
        messageReceived(json['message'])        # On the console

        # Get and sent back a response to the chat interface
        agentMessage = agent.getResponse(sessionId, json['message'])
        sendMessage(sessionId, agentMessage)
                
if __name__ == '__main__':
        # Takes optional host and port arguments but by default will listen on localhost:5000
        socketio.run(app, host='0.0.0.0', port=5000, debug=True)
