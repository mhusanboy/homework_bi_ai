import pandas as pd
from pathlib import Path
current_dir = Path(__file__).resolve().parent



def problem1():
    df_json = pd.read_json(current_dir/'data/iris.json')
    df_json.columns = [column.lower() for column in df_json.columns]
    print(df_json[['sepallength', 'sepalwidth']])


def problem2():
    df_excel = pd.read_excel(current_dir/'data/titanic.xlsx')
    df_above_30 = df_excel[df_excel['Age'] > 30]
    print(df_above_30)
    print(df_excel['Sex'].value_counts())

def problem3():
    df_flights = pd.read_parquet(current_dir/'data/flights')
    print(df_flights['dest'].nunique())


def problem4():
    df_movies = pd.read_csv(current_dir/'data/movie.csv')
    above120 = df_movies[df_movies['duration']>120]
    print(above120)
    above120.sort_values(by='director_facebook_likes', inplace=True, ascending=False)
    print(above120)
