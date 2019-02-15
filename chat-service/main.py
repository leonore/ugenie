from flask import Flask, render_template, request
from flask_socketio import SocketIO

from model import agent

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#' # Secret key for encryption
socketio = SocketIO(app) # Apply SocketIO to 'app' to use it instead of app for running the application

# When the user enters the homepage ('/') it triggers the sessions view
@app.route('/')
def sessions():
        return render_template('session.html') # Helps render the HTML page, called a 'template'

def messageReceived(sessionId, message):
        print('Message received from', sessionId,': ', message)

def sendMessage(sessionId, message):
        print('Sending message!')
        json = {'user_name' : 'GUVA', 'message' : message}
        socketio.emit('bot_message', json)

@socketio.on('new_connection')
def handle_connection(json):
        print('User connected: ' + str(json))
        
        # Get the session ID this event is associated with
        sessionId = request.sid
        
        # Print the welcome message on the chat interface
        sendMessage(sessionId, "Hello, I'm GUVA, the Glasgow University Virtual Assistant. How can I help you?")
        
@socketio.on('new_message')
def handle_message(json):
        print('Received event: ' + str(json))

        # Get the session ID this event is associated with
        sessionId = request.sid
        
        # Print the message that was sent
        socketio.emit('user_message', json)            # On the chat interface
        messageReceived(sessionId, json['message'])     # On the console

        # Get and sent back a response to the chat interface
        agentMessage = agent.getResponse(sessionId, json['message'])
        sendMessage(sessionId, agentMessage)
                
if __name__ == '__main__':
        # Takes optional host and port arguments but by default will listen on localhost:5000
        socketio.run(app, host='0.0.0.0', port=5000, debug=True)
