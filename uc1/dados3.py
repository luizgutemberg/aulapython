import pandas as pd

df = pd.read_csv ('ClassicDisco.csv')

filtro_artist = df['Artist']
filtro_track = df['Track']
filtro_year = df['Year']
filtro_album = df['Album']

print (filtro_album, filtro_track, filtro_artist, filtro_year)
