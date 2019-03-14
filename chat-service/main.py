from flask import Flask, render_template, request, escape
from flask_socketio import SocketIO, join_room

from model import agent, network_config, chat_logger

import re
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#' # Secret key for encryption
socketio = SocketIO(app) # Apply SocketIO to 'app' to use it

# When the user enters the homepage ('/') it triggers the sessions view
@app.route('/')
def sessions():
        return render_template('session.html') # Helps render the HTML page, called a 'template'

def messageReceived(sessionId, message):
        print('Message received from',sessionId,':',message)
        chat_logger.logUser(sessionId, message)

def sendMessage(sessionId, message):
        # If the message contains button responses, put those in the json to send back to the chat
        if 'buttons' in message:
                print('Sending message: ',message['text'],' with buttons: ',message['buttons'])
                json = {'user_name' : 'UGenie', 'message' : message['text'], 'buttons' : message['buttons']}
                chat_logger.logAgent(sessionId, message['text'])
                chat_logger.logAgent(sessionId, message['buttons'])
        else:
                print('Sending message: ',message['text'])
                json = {'user_name' : 'UGenie', 'message' : message['text']}
                chat_logger.logAgent(sessionId, message['text'])

        socketio.emit('bot_message', json, room=sessionId)

@socketio.on('user_joined')
def handle_connection(json):
        # Print the event data about this new connection on the console
        print('User connected: ',json)

        # Get the session ID this event is associated with
        sessionId = request.sid

        # Print the welcome message on the chat interface
        sendMessage(sessionId, {'text': "Hello, I'm UGenie, the Glasgow University virtual assistant! How can I help you?",
                                'buttons': [{'payload': '/help', 'title': 'What can I ask you?'},
                                            {'payload': '/expert', 'title': 'I know what to ask you'}]})

@socketio.on('new_message')
def handle_message(json):
        start = time.time()

        # Get the session ID this event is associated with
        sessionId = request.sid

        # Print the message that was sent on the chat interface, after escaping potential XSS or HTML injections
        socketio.emit('user_message', {'user_name':'You', 'message':escape(json['message'])}, room=sessionId)
        # Print the message that was sent on the server console and in the chat log
        messageReceived(sessionId, json['message'])

        # Get a response from the agent and send it back to the chat interface
        # If the socket event contained a payload (button response), send that to the agent
        if 'payload' in json:
                agentMessages = agent.getResponse(sessionId, json['payload'])
        # Otherwise just send the message
        else:
                agentMessages = agent.getResponse(sessionId, json['message'])

        # If the agent took less than a second to respond then wait a second to prevent unpleasant immediate response
        end = time.time() - start
        secondsElapsed = end % 60
        if(secondsElapsed < 1):
                time.sleep(1-secondsElapsed)

        # Return Rasa's response / responses
        if(type(agentMessages) is dict):
                sendMessage(sessionId, agentMessages)
        else:
                for agentMessage in agentMessages:
                        start = time.time()
                        sendMessage(sessionId, agentMessage)
                        # Wait a while before sending each message to give user time to process
                        time.sleep(0.8)

if __name__ == '__main__':
        # Takes optional host and port arguments but by default will listen on localhost:5000
        socketio.run(app, host='0.0.0.0', port=5000, debug=True)
