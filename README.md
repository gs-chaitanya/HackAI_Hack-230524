# Fahrenheit 451: A Temperature Alert Agent
## Team ID: HackAI_Hack-230524
### Project Description
In this project, we use a decentralised model using the uAgents library by Fetch.AI.
We are using decentralised model for this project, thereby increasing modularity and reducing the risk of errors thus the Fetch.AI's uAgents library was extremely helpful in this scenario.

We have chosen to chosen the part 1 of PS, i.e. Temperature Alert Agent.
We have utilised the weatherstack API to fetch the real time temperature data of locations.
There are 2 bots:
  One bot interfaces with the user. Asks for the city and the max and min temperatures. THis bot then sends a message to the other bot which is the server bot
  The server bot makes the API calls to weatherstack and hence we have solved all the parts of the PS.

### Instructions to run Fahrenheit 451 Agent
1. Run the poetry shell
2. Install the required dependencies, use the command:
`pip install -r requirements.txt`
3. **IMPORTANT**: Run the server.py first of all.
`python server.py`
4. Then run main.py to use the Agent.
`python main.py`

#### Special considerations:
Ensure that the server.py file is run first of all, it is necessary in order for the main.py agent to function properly.

