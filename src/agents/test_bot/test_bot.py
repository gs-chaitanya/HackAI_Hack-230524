from uagents import Agent,Context,Model
from uagents.setup import fund_agent_if_low
from dotenv import load_dotenv
import requests
import os
load_dotenv()

ACCESS_KEY = os.getenv('ACCESS_KEY')
CITY_ID='New Delhi' # fetch from storage
maxT = 0
minT = 0
TEMPERATURE_BOT_ADDRESS=os.getenv('TEMPERATURE_BOT_ADDRESS')
class Message(Model):
    message:str

test_bot=Agent(name="Jigglypuff",seed="Jigglypuff",port=6969,endpoint=["http://127.0.0.1:6969/submit"])
fund_agent_if_low(test_bot.wallet.address())

@test_bot.on_interval(period=2.0)
async def message_temperature_bot(ctx:Context):
    await ctx.send(TEMPERATURE_BOT_ADDRESS,Message(message=CITY_ID))
    # ctx.logger.info("message sent!")

@test_bot.on_message(model=Message)
async def send_alert(ctx:Context,sender:str,msg:Message):
    recieved_temperature=int(msg.message)
    if(recieved_temperature < minT):
        ctx.logger.info(f"Too cold. Current temperature: {msg.message}")
    elif(recieved_temperature > maxT):
        ctx.logger.info(f"Too hot. Current temperature: {msg.message}")
    

    # put a function that checks if recieved_temperature is outside the range

    # ctx.logger.info(f"recieved temperature : {msg.message}")

if __name__=="__main__":
    CITY_ID = input("Enter City: ")
    api_url = "http://api.weatherstack.com/current"  
    params = {  
        "query": CITY_ID,
        "access_key":  ACCESS_KEY
    }
    response = requests.get(api_url, params=params)
    res =response.json()
    try:
        print(res['success'])
        print("Enter a valid city")
    
    except:
        maxT = int(input("Enter the maximum temperature: "))
        minT = int(input("Enter the minimum temperature: "))
        test_bot.run()

    