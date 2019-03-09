import datetime

def logUser(sessionId, message):
    now = datetime.datetime.now()
    with open('chat-logs/' + str(sessionId) + '.txt', 'w') as out:
        out.write(now.strftime('%y-%m-%d %H:%M') + ' User: ' + str(message) + '/r/n')

def logAgent(sessionId, message):
    now = datetime.datetime.now()
    with open('chat-logs/' + str(sessionId) + '.txt', 'w') as out:
        out.write(now.strftime('%y-%m-%d %H:%M') + ' ChatBot: ' + str(message) + '/r/n')
