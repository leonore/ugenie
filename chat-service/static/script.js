// Establish the connection and create the session
// document.domain represents the IP address of the computer you are working on and location.port represents the port
var socket = io.connect('http://' + document.domain + ':' + location.port);

// When the user connects, run this function
socket.on('connect', function() {
	console.log(socket.id);

	// Send an event to the server with details on the newly connected user
    socket.emit('user_joined', {
		id: socket.id
    });

	// When the user submits a new message, send a message event to the server
    var form = $('form').on('submit', function(e) {
        e.preventDefault();
		var messageInput = $('input.message-form-input');
		console.log('messageInput.val(): ', messageInput.val());
		// Check if the user has entered anything before sending a socket event for the message
		if(messageInput.val() !== ''){
			socket.emit('new_message', {
				user_name: 'You',
				message: messageInput.val()
			});
			messageInput.val('').focus();
		}
    });
})

var messageArea = $('div.message-area');

// When the client receives a 'user_message' event, print the message on the chat as a user message
socket.on('user_message', function(msg) {
    if (typeof msg.user_name !== 'undefined') {
        messageArea.append('<div class="message user-message">' + msg.message.autoLink() + '</div>');
		messageArea.scrollTop(messageArea.prop('scrollHeight'));
    }
})

// When the client receives a 'bot_message' event, print the message on the chat as a bot message
socket.on('bot_message', function(msg) {
    console.log(msg);
    if (typeof msg.user_name !== 'undefined') {
		messageArea.append('<div class="message bot-message">' + msg.message.autoLink() + '</div>');

		// If this message also contains button responses, render them
		if(typeof msg.buttons !== 'undefined'){
			messageArea.append('<div class="message button-area"></div>');
			var buttonArea = $('div.button-area');
			console.log(msg.buttons);
			for (var buttonIndex in msg.buttons) {
				var buttonObject = msg.buttons[buttonIndex];

				// If this button object is a title and not a payload, add it as a button, (might not still be needed to check but kept as doing no harm)
				if(typeof buttonObject.title !== 'undefined'){
					console.log(buttonObject);
					buttonArea.append('<button class="message reply-button" type="button" onclick="buttonReply(\'' + buttonObject.title + '\', \'' + buttonObject.payload + '\')">' + buttonObject.title + '</button>');
				}
			}
			
			// Disable the message field to prevent the user from inputting a message when they should be pressing a button
			$('input.message-form-input').prop('disabled', true).attr('placeholder', 'Press a button above');
		}
		
		messageArea.scrollTop(messageArea.prop('scrollHeight'));
    }
})


// JavaScript functions

function openForm() {
    document.getElementById('myForm').style.display = 'block';
    document.getElementsByClassName('open-button')[0].style.visibility = 'hidden';
}

function closeForm() {
    document.getElementById('myForm').style.display = 'none';
    document.getElementsByClassName('open-button')[0].style.visibility = 'visible';
}

function buttonReply(chosenButton, chosenPayload) {
	$('input.message-form-input').prop('disabled', false).attr('placeholder', 'Type a message...');
	$('.message.button-area').remove();
	socket.emit('new_message', {
		user_name: 'You',
		message: chosenButton,
		payload: chosenPayload
	});
}
