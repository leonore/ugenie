function openForm() {
    document.getElementById("myForm").style.display = "block";
    document.getElementsByClassName("open-button")[0].style.visibility = 'hidden';
}

function closeForm() {
    document.getElementById("myForm").style.display = "none";
    document.getElementsByClassName("open-button")[0].style.visibility = 'visible';
}

// Establish the connection and create the session
// document.domain represents the IP address of the computer you are working on and location.port represents the port
var socket = io.connect('http://' + document.domain + ':' + location.port);

// When the user connects, run this function
socket.on('connect', function() {
	// Sent an event to the server with details on the newly connected user
    socket.emit('new_connection', {
        state: 'User Connected',
		ip: document.domain
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
			})
			messageInput.val('').focus()
		}
    });
})

var messageArea = $('div.message-area');

// When the client receives a 'user_message' event, print the message on the chat as a user message
socket.on('user_message', function(msg) {
    if (typeof msg.user_name !== 'undefined') {
		console.log('msg.message: ', msg.message);
        messageArea.append('<div class="message user-message">' + msg.message + '</div>');
		messageArea.scrollTop(messageArea.prop('scrollHeight'));
    }
})

// When the client receives a 'user_message' event, print the message on the chat as a bot message
socket.on('bot_message', function(msg) {
    if (typeof msg.user_name !== 'undefined') {
        messageArea.append('<div class="message bot-message">' + msg.message + '</div>');
		messageArea.scrollTop(messageArea.prop('scrollHeight'));
    }
})
