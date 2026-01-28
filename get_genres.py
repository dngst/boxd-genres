import os
import csv
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('TMDB_API_KEY')
BASE_URL = 'https://api.themoviedb.org/3'

data = []
with open("watched.csv", "r") as infile:
    reader = csv.reader(infile)
    next(reader)
    for row in reader:
        name, year = row[1], row[2]
        search_r = requests.get(f'{BASE_URL}/search/movie', params={'api_key': api_key, 'query': name, 'year': year}).json()
        movie_id = search_r['results'][0]['id']
        genres = ', '.join(g['name'] for g in requests.get(f'{BASE_URL}/movie/{movie_id}', params={'api_key': api_key}).json()['genres'])
        data.append([name, year, genres])
        print(f"{name}: {genres}")

with open("movies_with_genres.csv", "w", newline='') as outfile:
    csv.writer(outfile).writerows([['name', 'year', 'genre']] + data)

