# chat/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):


    async def connect(self):
        print("haiiii")
        await self.accept()
        await self.channel_layer.group_add('chat_group', self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('chat_group', self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.channel_layer.group_send(
            'chat_group',
            {
                'type': 'chat.message',
                'message': message,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message,
        }))
