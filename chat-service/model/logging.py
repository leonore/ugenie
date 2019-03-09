import datetime

def logUser(sessionId, message):
    now = datetime.datetime.now()
    with open(str(sessionId)+".txt", "w") as out:
        out.write(now.strftime("%Y-%m-%d %H:%M") + " User: " + str(message))

def logAgent(sessionId, message):
    now = datetime.datetime.now()
    with open(str(sessionId)+".txt", "w") as out:
        out.write(now.strftime("%Y-%m-%d %H:%M") + " ChatBot: " + str(message))
