import json
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer

# class NotificationConsumer(AsyncWebsocketConsumer):

#     async def connect(self):
#         self.group_name = 'notification'

#         await self.channel_layer.group_add(self.group_name,self.channel_name)

#         await self.accept()


#     async def disconnect(self):
#         await self.channel_layer.group_discard(self.group_name,self.channel_name) 




#     async def recieve(self,text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message'],
#         event = {
#             'type': 'send_message',
#             'message': message
#         }

#         await self.channel_layer.group_send(self.group_name,event)

#     async def send_message(self,event):
#         message = event['message']

#         await self.send(text_data = json.dumps({'message':message}))    


class NotificationConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.send(text_data= json.dumps({
            'type':'connection established',
            'message':'you are now connected',
        }))

