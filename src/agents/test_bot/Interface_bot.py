from uagents import Agent,Context,Model
from uagents.setup import fund_agent_if_low
from dotenv import load_dotenv
import requests
import os

"""
This bot interfaces with the user and stores the parameters given by the user. It then sends the CITY parameter
to the temperature bot and then awaits its response. If the temperature received lies outside the user specified
range then it sends an alert.

"""

load_dotenv()

ACCESS_KEY = os.getenv('ACCESS_KEY')
maxT = 0
minT = 0
TEMPERATURE_BOT_ADDRESS=os.getenv('TEMPERATURE_BOT_ADDRESS')
class Message(Model):
    message:str

interface_bot=Agent(name="Jigglypuff",seed="Jigglypuff",port=6969,endpoint=["http://127.0.0.1:6969/submit"])
fund_agent_if_low(interface_bot.wallet.address())

@interface_bot.on_interval(period=2.0)
async def message_temperature_bot(ctx:Context):
    CITY_ID = ctx.storage.get('CITY')
    await ctx.send(TEMPERATURE_BOT_ADDRESS,Message(message=CITY_ID))

@interface_bot.on_message(model=Message)
async def send_alert(ctx:Context,sender:str,msg:Message):
    recieved_temperature=int(msg.message)
    minT = ctx.storage.get('MinTemp') # Fetch parameters from storage
    maxT = ctx.storage.get('MaxTemp')
    if(recieved_temperature < minT): # Make the alerts if condition is satisfied
        ctx.logger.info(f"ALERT! Too cold. Current temperature: {recieved_temperature}")
    elif(recieved_temperature > maxT):
        ctx.logger.info(f"ALERT! Too hot. Current temperature: {recieved_temperature}")
    



if __name__=="__main__":
    interface_bot.run()

    