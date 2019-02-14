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
	console.log('New connection from ' + document.domain);
	
	// Sent an event to the server with details on the newly connected user
    socket.emit('new_connection', {
        state: 'User Connected',
		ip: document.domain
    });
	
	// When the user submits a new message, send a message event to the server
    var form = $('form').on('submit', function(e) {
        e.preventDefault()
        socket.emit('new_message', {
			user_name: 'You',
            message: $('input.message-form-input').val()
        })
        $('input.message-form-input').val('').focus()
    });
})

// When the client receives a 'user_message' event, print the message on the chat as a user message
socket.on('user_message', function(msg) {
    console.log(msg);
    if (typeof msg.user_name !== 'undefined') {
        $('div.message-area').append('<div class="message user-message">' + msg.message + '</div>')
		$('div.message-area').scrollTop = $('div.message-area').scrollHeight;
    }
})

// When the client receives a 'user_message' event, print the message on the chat as a bot message
socket.on('bot_message', function(msg) {
    console.log(msg);
    if (typeof msg.user_name !== 'undefined') {
        $('div.message-area').append('<div class="message bot-message">' + msg.message + '</div>')
		$('div.message-area').scrollTop = $('div.message-area').scrollHeight;
    }
})
