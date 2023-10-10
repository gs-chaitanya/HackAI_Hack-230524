from uagents import Bureau, Context
from agents.temperature_bot.temperature_bot import temperature_bot
from agents.test_bot.Interface_bot import interface_bot
from Set_Bot_Params import Get_Bot_Params

maxT = 0
minT = 0
CITY = 0

@interface_bot.on_event("startup")
async def store_params(ctx:Context):  # Store the input given by the user
    ctx.storage.set("MinTemp", minT)
    ctx.storage.set("MaxTemp", maxT)
    ctx.storage.set("CITY", CITY)
    

if __name__ == "__main__":

    minT, maxT, CITY = Get_Bot_Params() # Take input from user

    if(CITY != -1):
        bureau = Bureau(endpoint=["http://127.0.0.1:42069/submit"], port=22095) # Create a bereau to manage bot interaction
        
        print(f"Activating {temperature_bot.name}")
        bureau.add(temperature_bot) 
        print(f"Activating {interface_bot.name}")
        bureau.add(interface_bot) # Add both bots
        bureau.run() # Run the bereau



