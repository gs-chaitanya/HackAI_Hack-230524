# Fahrenheit 451: A Temperature Alert Agent
## Team ID: HackAI_Hack-230524
### Project Description
In this project, we use a two bot model using the uAgents library by Fetch.AI.

We decided to go with part 1 of the PS, i.e. Temperature Alert Agent.

We have utilized the weatherstack API to fetch real-time temperature data of locations.
There are 2 bots:
  [Jigglypuff] interfaces with the user. Asks for the city and the max and min temperatures.

  This bot then sends a message to another bot [Chikorita], via the bureau functionality which then fetches data from the API. 
  This adds scalability to the project as we can increase the number of bots sending requests to the 
  temperature agent [Chikorita] by just adding them to the bureau.

### Instructions to run Fahrenheit 451 Agent
1. Run the poetry shell, use the command:
`poetry shell`
If the command does not run, please ensure that poetry is properly configured and added to path
2. Install the required dependencies, use the command:
`pip install -r requirements.txt`
4. Replace the ACCESS_KEY parameter in the .env file with a valid weatherstack API key. 
3. Run src/main.py to start the agents.
`python src/main.py`




