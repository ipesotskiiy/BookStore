# from channels.generic.websocket import AsyncWebsocketConsumer
#
#
# class FooConsumer(AsyncWebsocketConsumer):
#
#     async def websocket_connect(self, event):
#         user = self.scope['user']
#         await self.accept()

from channels.generic.websocket import AsyncWebsocketConsumer
import json
import socketio

import json

from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print('here we go1')
        self.accept()

    def disconnect(self, close_code):
        print('here we ne go1')
        pass

    def receive(self, text_data):
        print('here we receive')
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        self.send(text_data=json.dumps({"message": message}))