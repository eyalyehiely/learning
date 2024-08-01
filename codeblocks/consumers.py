# import json
# from channels.generic.websocket import AsyncWebsocketConsumer

# class CodeBlockConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.codeblock_id = self.scope['url_route']['kwargs']['codeblock_id']
#         self.room_group_name = f'codeblock_{self.codeblock_id}'

#         await self.channel_layer.group_add(
#             self.room_group_name,
#             self.channel_name
#         )

#         await self.accept()

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )

#     async def receive(self, text_data):
#         data = json.loads(text_data)
#         code = data.get('code', None)
#         role = data.get('role', None)

#         if code is not None & role is not None:
#             await self.channel_layer.group_send(
#                 self.room_group_name,
#                 {
#                     'type': 'code_update',
#                     'code': code,
#                     'type': 'role_update',
#                     'role': role,
#                 }
#             )
#         else:
#             await self.send(text_data=json.dumps({
#                 'error': 'Invalid data',
#             }))

#     async def code_update(self, event):
#         code = event['code']
#         await self.send(text_data=json.dumps({
#             'type': 'code_update',
#             'code': code,
#         }))

#     async def role_update(self, event):
#         role = event['role']
#         await self.send(text_data=json.dumps({
#             'type': 'role_update',
#             'role': role,
#         }))




import json
from channels.generic.websocket import AsyncWebsocketConsumer

class CodeBlockConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.codeblock_id = self.scope['url_route']['kwargs']['codeblock_id']
        self.room_group_name = f'codeblock_{self.codeblock_id}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        code = data.get('code', None)
        role = data.get('role', None)

        if code is not None:
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'code_update',
                    'code': code,
                }
            )
        if role is not None:
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'role_update',
                    'role': role,
                }
            )
        else:
            await self.send(text_data=json.dumps({
                'error': 'Invalid data',
            }))

    async def code_update(self, event):
        code = event['code']
        await self.send(text_data=json.dumps({
            'type': 'code_update',
            'code': code,
        }))

    async def role_update(self, event):
        role = event['role']
        await self.send(text_data=json.dumps({
            'type': 'role_update',
            'role': role,
        }))