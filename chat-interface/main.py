from flask import Flask, render_template, request
from flask_socketio import SocketIO

import agent
import actions

app = Flask(__name__) # Wrap Flask around __name__
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#' # Secret key for encryption
socketio = SocketIO(app) # Apply SocketIO to 'app' to use it instead of app for running the application

sessionAgents = {}

# When the user enters the homepage ('/') it triggers the sessions view
@app.route('/')
def sessions():
        return render_template('session.html') # Helps render the HTML page, called a 'template'

def messageReceived(message):
        print('Message received:', message)

def sendMessage(message):
        print('Sending message!')
        json = {'user_name' : 'GUVA', 'message' : message}
        socketio.emit('print message', json)

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
        print('Received event: ' + str(json))
        
        sessionId = request.sid

        # If this event is a user connection
        if ('state' in json and json['state'] == 'User Connected'):
                sessionAgents[sessionId] = agent.SessionAgent(sessionId)
                sendMessage("Hello, I'm GUVA, the Glasgow University Virtual Assisstant. How can I help you?")

        # If this event contains a message, answer it
        elif ('message' in json and json['message'] != ''):
                socketio.emit('print message', json)
                messageReceived(json['message'])
                sendMessage(sessionAgents[sessionId].getResponse(json['message']))
                
if __name__ == '__main__':
        # Train Rasa-Core Dialogue Model
        #agent.train()
        
        # Takes optional host and port arguments but by default will listen on localhost:5000
        socketio.run(app, debug=True)
