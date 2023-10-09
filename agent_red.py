from uagents import Agent,Context,Model
import requests  
  
def get_temprature( city_id):  
    api_url = "http://api.weatherstack.com/current"  
    params = {  
        "query": city_id,
        "access_key": "2c5669669f00e46e95e61b5ae18b4efa"  
    }
    response = requests.get(api_url, params=params)  
    print(response.status_code)
    data = response.json() 
    temperature = data['current']['temperature']
    return temperature

red = Agent(name="Red",seed="red phrase")

@red.on_interval(period=2.0)
async def period_func(ctx:Context):
    cur_temp=get_temprature('New Delhi')
    if(cur_temp<ctx.storage.get("min_range") or cur_temp>ctx.storage.get("max_range")):
        ctx.logger.info(f"current temprature [{cur_temp}] is out of range [{ctx.storage.get('min_range')} , {ctx.storage.get('max_range')}]")

if __name__ == "__main__":
    red.run()