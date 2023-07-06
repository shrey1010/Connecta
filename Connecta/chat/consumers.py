import json
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model


User = get_user_model()

class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print("connected",event)
        await self.send({
            'type': 'websocket.accept'
        })

    async def websocket_receive(self,event):
        print("recieve", event)
        recieved_data = json.loads(event['text'])
        msg = recieved_data.get["message"]
        if not msg:
            return False

        response = {
            'message': msg
        }
        await self.send({
            'type': 'websocket.send',
            'text': json.dumps(response)
        }) 
        


    async def websocket_disconnect(self,event):
        print("disconnected", event)

    