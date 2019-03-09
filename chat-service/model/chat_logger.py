import datetime

# Log a message from the user along with date and time
def logUser(sessionId, message):
    time = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    now = datetime.datetime.now()
    with open('model/chat-logs/' + str(sessionId) + '.txt', 'a') as out:
        out.write(time + ' User: ' + str(message) + '\r\n') 

# Log a message from the user along with date and time
def logAgent(sessionId, message):
    time = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    # If the bot returned a list of buttons, follow this procedure to log them
    if type(message) is list:
        buttonString = ''
        for button in message:
            buttonString += '(Button): ' + button['title'] + ' '
            with open('model/chat-logs/' + str(sessionId) + '.txt', 'a') as out:
                out.write(time + ' ChatBot: ' + str(buttonString) + '\r\n') 
    # Otherwise log the message as normal
    else:
        with open('model/chat-logs/' + str(sessionId) + '.txt', 'a') as out:
            out.write(time + ' ChatBot: ' + str(message) + '\r\n') 
