# NBA-2013-Analysis
NBA 2013 played scored points prediction URL: https://nba-2013-pntsprediction.herokuapp.com/

***Introduction***

Here we are creating a regressor model to predict the point scored by a NBA player. our dataset has 30 features and 1 target variable.

***The columns are:***

- PLAYER = Player Name (corresponds to name in 2013-2014 season)

- POS = Position of the player

- AGE = Age of the player

- BREF_TEAM_ID  = Team code

- G = Number of games the player has played

- GS = Number of games the player started

- MP = Minutes Played (higher for some teams that have played over time games)

- FG = Field Goals Made (number of baskets made not counting free throws)

- FGA = Field Goals Attempted (number of shots taken not counting free throws)

- FG. = Field Goal Percentage (column FG divided by column FGA)

- X3P = 3 Point Shots Made (shots made from beyond 3 point arc)

- X3PA = 3 Point Shots Attempted (shots taken from beyond 3 point arc)

- X3P. = 3 Point Shot Percentage (column X3P divided by column X3PA)

- X2P = 3 Point Shots Made (shots made from beyond 2 point arc)

- X2PA = 3 Point Shots Attempted (shots taken from beyond 2 point arc)

- X2P. = 3 Point Shot Percentage (column X2P divided by column X2PA)

- FT = Free Throws Made (total free foul shots made)

- FTA = Free Throws Attempted (total free foul shots taken)

- FT. = Free Throw Percentage (column FT divided by column FTA)

- ORB = Offensive Rebounds (missed team shots that were recovered)

- DRB = Defensive Rebounds (missed opponents’ shots that were recovered)

- REB = Rebounds (column ORB added to column DRB)

- AST = Assists (total field goals that were assisted on)

- STL = Steals (total opponents’ possessions taken away)

- BLK = Blocks (total number of opponents’ field goals blocked)

- TOV = Turnovers (total possessions given away)

- PF = Personal Fouls (total fouls commited by team)

- PTS = Pts Scored (total points scored throughout the season)

- SEASON = Year (year that season ends, from 2013 to 2014)

- SEASON_END = End of season 2013

### Instruction to run the file
***Step 1***
**Create and activate an environment**
- Using Conda <br>
conda create -n [your environment name] python=3.7 <br>
Then activate the environment by writing <br>
conda activate [your environment name] <br>

- Using default Environments <br>
python3 -m venv [your environment name] <br>
Then activate the environment by writing <br>
[your environment name]\Scripts\activate.bat [For windows users] <br>
source [your environment name]/bin/activate [For Mac/Ubuntu users] <br>

NOTE: you can give any python version and ignore brackets while giving environment name

***Step 2***
**Install Dependencies**
- For library installations  write <br>
pip install -r requirements.txt 

***Step 3***
**Run The File**
- To run the file write <br>
python app.py
