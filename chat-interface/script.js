function openForm() {
    document.getElementById("myForm").style.display = "block";
    document.getElementsByClassName("open-button")[0].style.visibility = 'hidden';
}

function closeForm() {
    document.getElementById("myForm").style.display = "none";
    document.getElementsByClassName("open-button")[0].style.visibility = 'visible';
}

function Chat() {
    this.update = updateChat; // Ask the server if there are new lines in the text file.
    this.send = sendChat; // Called when a message is sent.
    this.getState = getStateOfChat; // Ask the server how many lines the current text file is, so it has something to compare against and know when lines are "new" or not.
}

function getStateOfChat() {
    if (!instance) {
        instance = true;
        $.ajax({
            type: "POST",
            url: "process.php",
            data: {
                'function': 'getState',
                'file': file
            },
            dataType: "json",
            success: function(data) {
                state = data.state;
                instance = false;
            }
        });
    }
}

function updateChat() {
    if (!instance) {
        instance = true;
        $.ajax({
                type: "POST",
                url: "process.php",
                data: {
                    'function': 'update',
                    'state': state,
                    'file': file
                },
                dataType: "json",
                success: function(data) {
                    if (data.text) {
                        for (var i = 0; i < data.text.length; i++) {
                            $('#chat-area').append($(""+ data.text[i] +""));
                            }
                        }
                        document.getElementById('chat-area').scrollTop = document.getElementById('chat-area').scrollHeight;
                        instance = false;
                        state = data.state;
                    }
        });
    }
    else {
        setTimeout(updateChat, 1500);
    }
}

function sendChat(message, nickname) {
    updateChat();
    $.ajax({
        type: "POST",
        url: "process.php",
        data: {
            'function': 'send',
            'message': message,
            'nickname': nickname,
            'file': file
        },
        dataType: "json",
        success: function(data) {
            updateChat();
        }
    });
}
