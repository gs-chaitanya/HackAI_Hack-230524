import requests
import os


def Get_Bot_Params():
    ACCESS_KEY = os.getenv('ACCESS_KEY')

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
        return 0, 0, -1

    except:
        maxT = int(input("Enter the maximum temperature: "))
        minT = int(input("Enter the minimum temperature: "))
        return minT, maxT, CITY_ID