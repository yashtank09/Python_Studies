#pip install pandas
import pandas as pd
songs = pd.read_csv('songs.csv')

print(max(songs['duration']))

print(min(songs['duration']))

print(songs.loc[songs['language']=='Hindi'])

print(songs.sort_values('songname'))

print(songs.iloc[2])