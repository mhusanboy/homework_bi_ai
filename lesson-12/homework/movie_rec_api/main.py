import os 
import requests
import random


base_url = "https://api.themoviedb.org/3/"

reader_token = os.environ.get('MOVIE_READ_ACCESS_TOKEN')
api_key = os.environ.get('MOVIE_API_KEY')

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {reader_token}"
}

genres = requests.get(base_url + 'genre/movie/list?language=en', headers=headers).json()['genres']

def get_genre_id(g):
    for genre in genres:
        # print(genre['name'].split())
        if genre['name'].lower() == g.lower() or g.lower() in [c.lower() for c in genre['name'].split()]:
            return str(genre['id'])
    return '-1'

def get_movies_by_genres(genre):
    response = requests.get(base_url + 'discover/movie', params={'with_genres' : ','.join(get_genre_id(s) for s in genre)}, headers=headers).json()
    return response['results']


# print(get_genre_id('fiction'))
user_genres = input("input genres to filter a random movie by genre(s) (space separated): ").split()

movies = get_movies_by_genres(user_genres)

if movies:
    movie = random.choice(movies)
    print(f"Original title: {movie['original_title']}")
    print(f"Title (en): {movie['title']}")
    print(f'Release date: {movie['release_date']}')
    print(f'Overview: {movie['overview']}')
    
else:
    print("No movies found with those genres.")

start