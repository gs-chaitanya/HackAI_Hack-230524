from uagents import Bureau, Context
from agents.temperature_bot.temperature_bot import temperature_bot
from agents.test_bot.Interface_bot import interface_bot
from Set_Bot_Params import Get_Bot_Params

maxT = 0
minT = 0
CITY = 0

@interface_bot.on_event("startup")
async def send_address(ctx:Context):
    ctx.storage.set("MinTemp", minT)
    ctx.storage.set("MaxTemp", maxT)
    ctx.storage.set("CITY", CITY)
    

if __name__ == "__main__":

    minT, maxT, CITY = Get_Bot_Params()

    if(CITY != -1):
        bureau = Bureau(port=420)
        print(f"Activating {temperature_bot.name}")
        
        bureau.add(temperature_bot)
        print(f"Activating {interface_bot.name}")
        bureau.add(interface_bot)
        bureau.run()



