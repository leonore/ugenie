from flask import Flask, render_template
from flask_socketio import SocketIO
from sample_query import get_fee, get_description
from difflib import SequenceMatcher

app = Flask(__name__) # Wrap Flask around __name__
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#' # Secret key for encryption
socketio = SocketIO(app) # Apply SocketIO to 'app' to use it instead of app for running the application

# When the user enters the homepage ('/') it triggers the sessions view
@app.route('/')
def sessions():
	return render_template('session.html') # Helps render the HTML page, called a 'template'

def messageReceived(message):
	print('Message received:', message)

def sendMessage(message):
	print('Sending message!')
	json = {}
	json['user_name'] = "GUVA"
	json['message'] = message
	socketio.emit('print message', json)

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
	print('Received event: ' + str(json))

	# If this event is a user connection
	if 'state' in json:
		sendMessage("Hello, I'm GUVA, the Glasgow University Virtual Assisstant. How can I help you?")

	# If this event contains a message, answer it
	elif ('message' in json and json['message'] != ''):
                socketio.emit('print message', json)
                messageReceived(json['message'])
                sendMessage(respond(json['message']))
		
# Remove these and use sample_query file after database is working
intents = {
        get_fee: ("how much is ", "how much are the fees for "),
        get_description: ("tell me about ", "what's the description for ")
}

def respond(message):
        highest_match = 0
        message = message.lower()
        for intent in intents.keys():
                for question in intents[intent]:
                        similarity = SequenceMatcher(None, message, question).ratio()
                        print('similar(',message,',',question,') = ', similarity)
                        if similarity > highest_match:
                                highest_match = similarity
        if highest_match > 0.4:
                for intent in intents.keys():
                        for question in intents[intent]:
                                if highest_match == SequenceMatcher(None, message, question).ratio():
                                        print('Most likely intent: ', intent)
                                        print('Most likely entity: ', message.replace(question, ''))
                                        return intent(message.replace(question, ''))
        else:
                return "Sorry, I couldn't understand what you said, could you please rephrase that?"

if __name__ == '__main__':
	# Takes optional host and port arguments but by default will listen on localhost:5000
	socketio.run(app, debug=True)
