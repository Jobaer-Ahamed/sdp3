from channels.generic.websocket import AsyncJsonWebsocketConsumer
#from channels.asgi import get_channel_layer
import random
from gameMain.gamelogic import * 

class gameConsumer(AsyncJsonWebsocketConsumer):

    gameboard = {
        0: '', 1: '', 2: '',3: '', 4: '', 5: '',6: '', 7: '', 8: '',
    }


    async def connect(self):
        print(self.scope["url_route"]['kwargs']['id'])
        self.room_code= self.scope["url_route"]['kwargs']['id']
        self.group_name= f"group_{self.room_code}"
  
        try:
            if len(self.channel_layer.groups[self.group_name])>=2:

                await self.accept()
                await self.send_json({
                    "event":"show_error",
                    "error":"This Room Is Full"
                })
                return await self.close(1)
            
                
           
            
        except KeyError:{
                
        }
        
        await self.accept()
        await self.channel_layer.group_add(self.group_name,self.channel_name)
        
        
        if len(self.channel_layer.groups[self.group_name])==2:
            temGroup = list(self.channel_layer.groups[self.group_name])
            print(temGroup)
            first_player = random.choice(temGroup)
            temGroup.remove(first_player)
            second_player = temGroup[0]
            final_Group= [first_player,temGroup[0]]
            print(final_Group)

            for i, channel_name in enumerate(final_Group):

                await self.channel_layer.send(channel_name,{
                 "type": "gameData.send",
                 "data": {
                 "event" : "startGame",
                 "gameboard": self.gameboard,
                 "myTurn": True if i==0 else False
                }  
            })

    async def receive_json(self,content, **kwargs):
        
        if(content['event']== "boardData_send"):

            winner = Is_win(content["gameboard"])
        
            if (winner):
              return await self.channel_layer.group_send(self.group_name, {
                    "type": "gameData.send",
                    "data": {
                    "event" :"won",
                    "gameboard": content['gameboard'],
                    "winner": winner,
                    "myTurn": False,
                    }
                })

            elif(Is_draw(content['gameboard'])):
                 return await self.channel_layer.group_send(self.group_name, {
                    "type": "gameData.send",
                    "data": {
                    "event" :"draw",
                    "gameboard": content['gameboard'],
                    "myTurn": False,
                    }
                })

          
        
            for channel_name in self.channel_layer.groups[self.group_name]:
                await self.channel_layer.send(channel_name, {
                    "type": "gameData.send",
                    "data": {
                    "event" : "boardData_send",
                    "gameboard": content['gameboard'],
                    "myTurn": False if self.channel_name== channel_name else True
                    }
                })  
        
        
    
    async def disconnect(self,code):
        
        await self.channel_layer.group_discard(self.group_name,self.channel_name)
        await self.channel_layer.group_send(self.group_name, {
            "type": "gameData.send",
            "data": {
            "event" :"friend_left",
            "gameboard": self.gameboard,
            "myTurn": False,
            }
        })
       
    async def gameData_send(self,event):
        await self.send_json(event['data'])
        