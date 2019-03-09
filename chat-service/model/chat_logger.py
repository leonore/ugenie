import datetime

def logUser(sessionId, message):
    time = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    now = datetime.datetime.now()
    with open('model/chat-logs/' + str(sessionId) + '.txt', 'a') as out:
        out.write(time + ' User: ' + str(message) + '\r\n') 

def logAgent(sessionId, message):
    time = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    print('agent message: ', message)
    if type(message) is list:
        buttonString = ''
        for button in message:
            buttonString += '(Button): ' + button['title'] + ' '
            with open('model/chat-logs/' + str(sessionId) + '.txt', 'a') as out:
                out.write(time + ' ChatBot: ' + str(buttonString) + '\r\n') 
    else:
        with open('model/chat-logs/' + str(sessionId) + '.txt', 'a') as out:
            out.write(time + ' ChatBot: ' + str(message) + '\r\n') 
