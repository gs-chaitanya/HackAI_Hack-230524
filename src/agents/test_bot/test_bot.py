from uagents import Agent,Context,Model
from uagents.setup import fund_agent_if_low
from dotenv import load_dotenv
import os
load_dotenv()

CITY_ID='New Delhi' # fetch from storage
TEMPERATURE_BOT_ADDRESS=os.getenv('TEMPERATURE_BOT_ADDRESS')
class Message(Model):
    message:str

test_bot=Agent(name="Jigglypuff",seed="Jigglypuff",port=6969,endpoint=["http://127.0.0.1:6969/submit"])
fund_agent_if_low(test_bot.wallet.address())

@test_bot.on_interval(period=2.0)
async def message_temperature_bot(ctx:Context):
    await ctx.send(TEMPERATURE_BOT_ADDRESS,Message(message=CITY_ID))
    ctx.logger.info("message sent!")

@test_bot.on_message(model=Message)
async def send_alert(ctx:Context,sender:str,msg:Message):
    recieved_temperature=int(msg.message)

    # put a function that checks if recieved_temperature is outside the range

    ctx.logger.info(f"recieved temperature : {msg.message}")

if __name__=="__main__":
    test_bot.run()