# consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class CodeBlockConsumer(AsyncWebsocketConsumer):
    connected_users = set()

    async def connect(self):
        self.codeblock_id = self.scope['url_route']['kwargs']['codeblock_id']
        self.room_group_name = f'codeblock_{self.codeblock_id}'

        # Add the user to the connected users set
        self.connected_users.add(self.channel_name)

        # Determine the role of the user
        if len(self.connected_users) == 1:
            self.role = 'mentor'
        else:
            self.role = 'student'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        # Send the role to the client
        await self.send(text_data=json.dumps({
            'role': self.role
        }))

    async def disconnect(self, close_code):
        # Remove the user from the connected users set
        self.connected_users.remove(self.channel_name)

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        code = data['code']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'code_update',
                'code': code,
            }
        )

    async def code_update(self, event):
        code = event['code']

        await self.send(text_data=json.dumps({
            'code': code,
        }))
