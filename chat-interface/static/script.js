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
socket.on('connect', function() {
	console.log('New connection from ' + document.domain);
    socket.emit('event', {
        state: 'User Connected',
		ip: document.domain
    })
    var form = $('form').on('submit', function(e) {
        e.preventDefault()
        let user_name = 'You'
        let user_input = $('input.message-form__input').val()
        socket.emit('event', {
			user_name: user_name,
            message: user_input
        })
        $('input.message-form__input').val('').focus()
    })
})
socket.on('print message', function(msg) {
    console.log(msg)
    if (typeof msg.user_name !== 'undefined') {
        $('div.messages').append('<div><b style="color: #000">' + msg.user_name + ': </b> ' + msg.message + '</div>')
		$('div.messages').scrollTop = $('div.messages').scrollHeight;
    }
})
