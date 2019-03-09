import datetime

def logUser(sessionId, message):
    now = datetime.datetime.now()
    out = open('chat-logs/' + str(sessionId) + '.txt', 'w')
    out.write(now.strftime('%y-%m-%d %H:%M') + ' User: ' + str(message) + '/r/n') 
    out.close() 

def logAgent(sessionId, message):
    now = datetime.datetime.now()
    out = open('chat-logs/' + str(sessionId) + '.txt', 'w')
    out.write(now.strftime('%y-%m-%d %H:%M') + ' ChatBot: ' + str(message) + '/r/n') 
    out.close() 
