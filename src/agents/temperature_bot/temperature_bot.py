from uagents import Agent,Context,Model
from uagents.setup import fund_agent_if_low
import requests
import os
from dotenv import load_dotenv

"""
This is the code for the temperature bot. This bot is responsible for making API calls based on the requests
sent to it by another bot. This bot sends the temperature info back to the bot making the requests
"""


load_dotenv()

class Message(Model):
    message:str

ACCESS_KEY = os.getenv('ACCESS_KEY')

def get_temperature( city_id):  # Makes api call to get temperature from a given city
    api_url = "http://api.weatherstack.com/current"  
    params = {  
        "query": city_id,
        "access_key":  ACCESS_KEY
    }
    response = requests.get(api_url, params=params)  
    data = response.json() 
    temperature = data['current']['temperature']
    return temperature

 
temperature_bot=Agent(name="Chikorita",seed="Chiokrita",port=42069,endpoint=["http://127.0.0.1:42069/submit"]) # Create the bot
fund_agent_if_low(temperature_bot.wallet.address())

@temperature_bot.on_message(model=Message) # When a message is received
async def handle_message(ctx: Context, sender: str, msg: Message):
    temperature=get_temperature(msg.message)
    ctx.logger.info(f"recieved request : {msg.message}")
    await ctx.send(sender,Message(message=temperature)) # Send the temperature info to the interface bot

if __name__=="__main__":
    temperature_bot.run()