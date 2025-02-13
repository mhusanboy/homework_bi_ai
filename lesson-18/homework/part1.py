import pandas as pd 
import sqlite3
from pathlib import Path
current_dir = Path(__file__).resolve().parent



def problem1():
    with sqlite3.connect(current_dir/'data/chinook.db') as connection:
        df_curstomers = pd.read_sql(
            "Select * from customers", 
            con=connection
        )
    print(df_curstomers.head(10))

def problem2():
    df_json = pd.read_json(current_dir/'data/iris.json')
    print("Shape:", df_json.shape)
    print("Header: ", ",".join(df_json.columns))

def problem3():
    df_excel = pd.read_excel(current_dir/'data/titanic.xlsx')
    print(df_excel.head())

def problem4():
    df_flights = pd.read_parquet(current_dir/'data/flights')
    print(df_flights.info())

def problem5():
    df_movies = pd.read_csv(current_dir/'data/movie.csv')
    print(df_movies.sample(10))
