import sys

sys.path.append('../chat-service/')
import unittest
import main

from flask import Flask, session, request, json as flask_json
from flask_socketio import SocketIO, send, emit


class TestSocketIO(unittest.TestCase):

    # testing a connection to the rasa agent
    def test_handle_connection(self):
        client = main.socketio.test_client(main.app)
        client.emit('user_joined','json')
        received = client.get_received()
        print(received)
        expected_data = {"Hello, I'm UGenie,"}
        self.assertEqual("Hello, I'm UGenie," in received[0]['args'][0]['message'], True)
        self.assertEqual(len(received), 1)

    # testing sending message to the rasa agent
    def test_new_message(self):
        client = main.socketio.test_client(main.app)
        client.emit('new_message', {'user_name' : 'you','message':"hi"})
        received = client.get_received()
        self.assertEqual(len(received), 2)
        print(received[0]['args'])
        print(received[1]['args'])
        self.assertEqual('Hi' in received[1]['args'][0]['message'] or 'Hello' in received[1]['args'][0]['message'],True)


if __name__ == '__main__':
    unittest.main()
