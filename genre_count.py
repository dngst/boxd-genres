import pandas as pd

df = pd.read_csv('movies_with_genres.csv')

genre_counts = df['genre'].str.split(', ').explode().value_counts()
print(genre_counts.to_string())
