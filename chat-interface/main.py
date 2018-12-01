from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__) # Wrap Flask around __name__
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#' # Secret key for encryption
socketio = SocketIO(app) # Apply SocketIO to 'app' to use it instead of app for running the application 	
# When the user enters the homepage ('/') it triggers the sessions view
@app.route('/')
def sessions():
	return render_template('session.html') # Helps render the HTML page, called a 'template'

def messageReceived(methods=['GET', 'POST']):
	print('Message received!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
	print('Received event: ' + str(json))
	socketio.emit('My response', json, callback=messageReceived)

if __name__ == '__main__':
	# Takes optional host and port arguments but by efault will listen on localhost:5000
	socketio.run(app, debug==true) 
