import os

print(os.environ.get('DOCKER'))

if os.environ.get('DOCKER'): # DOCKER DEPLOYMENT
    actionIP = "http://action_server:5055/webhook"
    elasticIP = "http://elastic:9200"
else: # LOCAL DEPLOYMENT
    actionIP = "http://localhost:5055/webhook"
    elasticIP = "http://localhost:9200"

print(actionIP, elasticIP)
