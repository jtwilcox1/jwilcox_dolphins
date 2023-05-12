# File created by JT Wilcox 
# sources
# https://www.scaler.com/topics/pandas/how-to-install-pandas-in-python/
# https://automatetheboringstuff.com/
# https://www.activestate.com/blog/how-to-predict-nfl-winners-with-python/
# https://towardsdatascience.com/sports-reference-api-intro-dbce09e89e52

# goals
# predict the Miami Dolphins record for the 2023-2024 season based on stats from last year

# # import libraries
import os
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import sportsreference as sr
# from sklearn.model_selection import cross_val_score
# from sklearn.linear_model import LogisticRegression

#adding a new row using the next index value.

# defines all teams that were in the NFL in 2022
from sportsreference.nfl.teams import Teams
teams2022 = Teams(year = '2022')
print(dir(teams2022))

# imports entire schedule of dolphins in 2022 season
from sportsreference.nfl.schedule import Schedule
mia2022 = Schedule('MIA', year = 2022)
# this display it on the rows but it is not right now
mia2022.dataframe.head()

# import stats from the boxscore of all games
from sportsreference.nfl.boxscore import Boxscore
game_data = Boxscore('202209110MIA')
game_data = Boxscore('202209180MIA')
game_data = Boxscore('202209250MIA')
game_data = Boxscore('202209290CIN')
game_data = Boxscore('202210090NYJ')
game_data = Boxscore('202210160MIN')
game_data = Boxscore('202210230MIA')
game_data = Boxscore('202210300MIA')
game_data = Boxscore('202211060MIA')
game_data = Boxscore('202211130MIA')
game_data = Boxscore('202211270MIA')
game_data = Boxscore('202212040SF')
game_data = Boxscore('202212110LAC')
game_data = Boxscore('202212170BUF')
game_data = Boxscore('202212250GB')
game_data = Boxscore('202201010NE')
game_data = Boxscore('202201080MIA')


print(dir(game_data))
game_data.dataframe

# imports entire miami roster
from sportsreference.nfl.roster import Roster 
mia2022 = Roster('MIA', year = '2022')


               



