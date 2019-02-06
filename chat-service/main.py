from flask import Flask, render_template, request
from flask_socketio import SocketIO

from model import agent

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#' # Secret key for encryption
socketio = SocketIO(app) # Apply SocketIO to 'app' to use it instead of app for running the application

sessionAgents = {} # Associate Session IDs with Agent objects

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

@socketio.on('event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
        print('Received event: ' + str(json))

        # Get the session ID this event is associated with
        sessionId = request.sid

        # If this event is a new user connecting
        if ('state' in json and json['state'] == 'User Connected'):
                # Print the welcome message on the chat interface
                sendMessage("Hello, I'm GUVA, the Glasgow University Virtual Assisstant. How can I help you?")

                # Create an agent object for this session
                sessionAgents[sessionId] = agent.SessionAgent() 
                
        # If this event contains a message, answer it
        elif ('message' in json and json['message'] != ''):
                # Print the message that was sent
                socketio.emit('print message', json)    # On the chat interface
                messageReceived(json['message'])        # On the console

                # Get and sent back a response to the chat interface
                agentMessage = sessionAgents[sessionId].getResponse(json['message'])
                sendMessage(agentMessage)
                
if __name__ == '__main__':
        # Train Rasa-Core Dialogue Model
        #agent.train()

        # Takes optional host and port arguments but by default will listen on localhost:5000
        socketio.run(app, host='0.0.0.0', port=5000, debug=True)
