from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__) # Wrap Flask around __name__
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#' # Secret key for encryption
socketio = SocketIO(app) # Apply SocketIO to 'app' to use it instead of app for running the application 	

# When the user enters the homepage ('/') it triggers the sessions view
@app.route('/')
def sessions():
	return render_template('session.html') # Helps render the HTML page, called a 'template'

def messageReceived(message):
	print('Message received:', message)
	
def sendMessage():
	print('Sending message!')
	json = {}
	json['user_name'] = "GUVA"
	json['message'] = "I'm a robot lmao"
	socketio.emit('print message', json)

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
	print('Received event: ' + str(json))
	
	# Send the event back in case it needs to be shown on the chat
	socketio.emit('print message', json)
	
	# If this event contains a message, answer it
	if 'message' in json:
		messageReceived(json['message'])
		sendMessage()

if __name__ == '__main__':
	# Takes optional host and port arguments but by default will listen on localhost:5000
	socketio.run(app, debug=True) 
