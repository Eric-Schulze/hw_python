import pandas as pd
import numpy as np

#Number of players
#youngest players
#country with the most players

players_df = pd.read_csv('players.csv')
print('Number of Players: ' + str(players_df['player_id'].count()))
print('Youngest Player: ' + players_df[['name','birthdate']].sort_values(['birthdate'],ascending=False).head(1).to_string(index=False,header=False))
print('Country with Most Players: ' + players_df['country_id'].value_counts().iloc[:1].to_string())