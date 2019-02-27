import requests

try:
    r = requests.get('http://34.73.120.65:9200', timeout=2.0)
except Exception as e:
    print("Elastic database inaccessible from outside. All good!")
else:
    assert False, ("Error! Please check database ports, they should not be exposed...")

try:
    r = requests.get('http://34.73.120.65:5055', timeout=2.0)
except Exception as e:
    print("Action server inaccessible from outside. All good!")
else:
    assert False, ("Error! Please check action server ports, they should not be exposed...")


try:
    r = requests.get('http://34.73.120.65:5000', timeout=5.0)
except Exception as e:
    assert False, ("Error! Please check Google VM, there seems to be a problem...")
else:
    print("Chatbot seems up. All good!")
