# Topic - Routing
from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import json 
from .models import Group,Chat
class MySyncConsumer(SyncConsumer):
  def websocket_connect(self, event):
    print('Websocket Connected...', event)
    print("xxxxxxxxxxxxxxxx",self.channel_layer)
    print(self.channel_name)
    self.group_name = self.scope['url_route']['kwargs']['groupkaname']
    async_to_sync(self.channel_layer.group_add)(
       self.group_name, 
       #'programer',    # group name
      self.channel_name
      )
    self.send({
      'type':'websocket.accept'
    })
    # def websocket_receive(self, event):
    #   print('Message Received from Client...', event['text'])
    #   print('Type of Message Received from Client...', type(event['text']))
    #   data = json.loads(event['text'])
    #   print("Data...", data)
    #   print("Type of Data...", type(data))
    #   print("Chat Message", data['msg'])
    #   # Find Group Object
    #   group = Group.objects.get(name = self.group_name)
    #   # Create New Chat Object
    #   chat = Chat(
    #     content = data['msg'],
    #     group = group
    #   )
    #   chat.save()
    
  def websocket_receive(self, event):
    print('Messaged Received...', event)
    print('Messaged is  recievd from posman', event['text'])
   # print('Type of Message Received from Client...', type(event['text']))
    # self.send({"type":"websocket.send",
    # "text":"messsage From rashid How are your posman"})
    self.group_name = self.scope['url_route']['kwargs']['groupkaname']
    data = json.loads(event['text'])
    print("Data...", data)
    print("Type of Data...", type(data))
    print("Chat Message", data['msg'])
    print("userrrrrrrrrrrrrrrrrrrrrrrrrrr",self.scope['user']) #gaetting username
    # Find Group Object
    group = Group.objects.get(name = self.group_name)
    if self.scope['user'].is_authenticated:
    # Create New Chat Object
      chat = Chat(
        content = data['msg'],
        group = group
        )
      chat.save()
      data['user'] = self.scope['user'].username
      print("Complete Data...", data)
      print("Type of Complete Data...", type(data))
      async_to_sync(self.channel_layer.group_send)(
          self.group_name,
          # 'programer',  
        # 'p, 
        {
          'type': 'chat.message',
          'message':json.dumps(data) #convert dict string
          # 'message':event['text']
        }
      )
    else:
      self.send({
        'type':'websocket.send',
        'text': json.dumps({"msg":"Login Required",
        "user":"unkownUser"})
      })
  
  
  def chat_message(self, event):
    print('Event...', event)
    print('Actual Data...', event['message'])
    print('Type of Actual Data...', type(event['message']))
    self.send({
      'type': 'websocket.send',
      'text': event['message']
    })


  def websocket_disconnect(self, event):
    print('Websocket Disconnected...', event)
    async_to_sync(self.channel_layer.group_discard)(
      self.group_name, 
      self.channel_name
      )
    raise StopConsumer()

class MyAsyncConsumer(AsyncConsumer):
  async def websocket_connect(self, event):
    print('Websocket Connected...', event)
  
    await self.send({
      'type':'websocket.accept'
    #  'text':'thrugh Asyncorus'
  
    })
    
  async def websocket_receive(self, event):
    print('Messaged Received...', event)
    print('Messaged is ', event['text'])
    await self.send({
       "type":"websocket.send",
      'text':'thrugh Asyncorus'
  
    })


  async def websocket_disconnect(self, event):
    print('Websocket Disconnected...', event)
    raise StopConsumer()


























# from channels.consumer import SyncConsumer
# class MySyncConsumer(SyncConsumer):

#   def websocket_connect(self, event):
#     print('WebSocket Connect...')

#   def websocket_receive(self, event):
#     print('Websocket Received...')
    
#   def websocket_disconnect(self, event):
#     print('Websocket Disconnect...')
