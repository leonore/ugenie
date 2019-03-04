from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room

from model import agent, network_config

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#' # Secret key for encryption
socketio = SocketIO(app) # Apply SocketIO to 'app' to use it instead of app for running the application

# When the user enters the homepage ('/') it triggers the sessions view
@app.route('/')
def sessions():
        return render_template('session.html') # Helps render the HTML page, called a 'template'

def messageReceived(sessionId, message):
        print('Message received from',sessionId,': ',message)

def sendMessage(sessionId, message):
        print('message: ',message)

        # If the message contains button responses, put those in the json to send back to the chat
        if 'buttons' in message:
                print('Sending message: ',message['text'],' with buttons: ',message['buttons'])
                json = {'user_name' : 'GUVA', 'message' : message['text'], 'buttons' : message['buttons']}
        else:
                print('Sending message: ',message['text'])
                json = {'user_name' : 'GUVA', 'message' : message['text']}

        socketio.emit('bot_message', json)

@socketio.on('user_joined')
def handle_connection(json):
        print('User connected: ',json)

        # Get the session ID this event is associated with
        sessionId = request.sid

        # Print the welcome message on the chat interface
        sendMessage(sessionId, {'text': "Hello, I'm GUVA, the Glasgow University Virtual Assistant. How can I help you?"})

@socketio.on('new_message')
def handle_message(json):
        print('Received event: ',json)

        # Get the session ID this event is associated with
        sessionId = request.sid

        # Print the message that was sent
        socketio.emit('user_message', json, room=sessionId)     # On the chat interface
        messageReceived(sessionId, json['message'])             # On the console

        # Get a response from the agent and send it back to the chat interface
        # If the socket event contained a payload (button response), send that to the agent
        if 'payload' in json:
                agentMessage = agent.getResponse(sessionId, json['payload'])
        # Otherwise just send the message
        else:
                agentMessage = agent.getResponse(sessionId, json['message'])
        sendMessage(sessionId, agentMessage)

if __name__ == '__main__':
        # Takes optional host and port arguments but by default will listen on localhost:5000
        socketio.run(app, host='0.0.0.0', port=5000, debug=True)
