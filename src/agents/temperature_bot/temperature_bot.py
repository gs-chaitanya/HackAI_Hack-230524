from uagents import Agent,Context,Model
from uagents.setup import fund_agent_if_low
import requests
import os
from dotenv import load_dotenv
load_dotenv()

class Message(Model):
    message:str

ACCESS_KEY = os.getenv('ACCESS_KEY')

def get_temperature( city_id):  
    api_url = "http://api.weatherstack.com/current"  
    params = {  
        "query": city_id,
        "access_key":  ACCESS_KEY
    }
    response = requests.get(api_url, params=params)  
    print(response.status_code)
    data = response.json() 
    temperature = data['current']['temperature']
    return temperature

temperature_bot=Agent(name="Chikorita",seed="Chiokrita",port=42069,endpoint=["http://127.0.0.1:42069/submit"])
fund_agent_if_low(temperature_bot.wallet.address())

@temperature_bot.on_event("startup")
async def send_address(ctx:Context):
    ctx.logger.info(f"address : {ctx.address}")


@temperature_bot.on_message(model=Message)
async def handle_message(ctx: Context, sender: str, msg: Message):
    temperature=get_temperature(msg.message)
    ctx.logger.info(f"recieved message : {msg.message}")
    # put city validation here
    await ctx.send(sender,Message(message=temperature))
    ctx.logger.info("message sent!")

if __name__=="__main__":
    temperature_bot.run()