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
        messageArea.append('<div class="message user-message">' + msg.message + '</div>');
		messageArea.scrollTop(messageArea.prop('scrollHeight'));
    }
})

// When the client receives a 'user_message' event, print the message on the chat as a bot message
socket.on('bot_message', function(msg) {
    console.log(msg);
    if (typeof msg.user_name !== 'undefined') {
		messageArea.append('<div class="message bot-message">' + msg.message + '</div>');
		
		// If this message also contains button responses, render them
		if(typeof msg.buttons !== 'undefined'){
			messageArea.append('<div class="message button-area"></div>');
			var buttonArea = $('div.button-area');
			console.log(msg.buttons);
			for (var buttonIndex in msg.buttons) {
				var buttonTitleObject = msg.buttons[buttonIndex];
				var buttonPayloadObject = msg.buttons[parseInt(buttonIndex)+1];
				
				// If this button object is a title and not a payload, add it as a button
				if(typeof buttonTitleObject.title !== 'undefined'){
					console.log(buttonTitleObject);
					console.log(buttonPayloadObject);
					buttonArea.append('<button class="message reply-button" type="button" onclick="buttonReply(\'' + buttonTitleObject.title + '\', \'' + buttonPayloadObject.payload + '\')">' + buttonTitleObject.title + '</button>');
				}
				
			}
		}

		messageArea.scrollTop(messageArea.prop('scrollHeight'));
    }
})


// JavaScript functions

function openForm() {
    document.getElementById("myForm").style.display = "block";
    document.getElementsByClassName("open-button")[0].style.visibility = 'hidden';
}

function closeForm() {
    document.getElementById("myForm").style.display = "none";
    document.getElementsByClassName("open-button")[0].style.visibility = 'visible';
}

function buttonReply(chosenButton, chosenPayload) {
	$(".message.button-area").remove();
	socket.emit('new_message', {
		user_name: 'You',
		message: chosenButton,
		payload: chosenPayload
	});
}
