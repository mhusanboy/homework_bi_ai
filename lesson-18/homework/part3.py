import pandas as pd 
from pathlib import Path
current_dir = Path(__file__).resolve().parent


def problem1():
    df_json = pd.read_json(current_dir/'data/iris.json')
    print(df_json.select_dtypes('number').describe().loc[['mean','50%', 'std']])

def problem2():
    df_excel = pd.read_excel(current_dir/'data/titanic.xlsx')
    print(df_excel['Age'].agg(['min', 'max', 'sum']))
    

def problem3():
    df_movies = pd.read_csv(current_dir/'data/movie.csv')
    print(df_movies.groupby('director_name')['director_facebook_likes'].sum().idxmax())
    sorted_by_length = df_movies.sort_values(by='duration', ascending=False)
    print(sorted_by_length[['movie_title','director_name']].head())
    

def problem4():
    df_flights = pd.read_parquet(current_dir/'data/flights')
    for column in df_flights.select_dtypes('number').columns:
        df_flights[column].fillna(df_flights[column].mean(), inplace=True)
    