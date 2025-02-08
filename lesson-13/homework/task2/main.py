import sqlite3
import os
from pathlib import Path

current_dir = Path(__file__).resolve().parent 

with sqlite3.connect(current_dir/'library.db') as con:
    cursor = con.cursor()
    books_table = """
        drop table if exists Books;
        create table Books(Title text, Author text, Year_Published int, genre text);
    """
    cursor.executescript(books_table)

    values = [
        ('To Kill a Mockingbird', 'Harper Lee', 1960,'Fiction'),
        ('1984', 'George Orwell', 1949, 'Dystopian'),
        ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic')
    ]
    cursor.executemany('Insert into books values(?, ?, ?, ?)', values)

    update_st = "Update books set year_published = 1950 where year_published = 1984"
    cursor.execute(update_st)

    query_st = "select title, author from books where genre = 'Dystopian'"
    print(cursor.execute(query_st).fetchall())

    delete_st = "delete from books where year_published < 1950"
    cursor.execute(delete_st)

    new_col = "Alter table books add column Rating real"
    ratings = [
        (4.8, 'To Kill a Mockingbird'),
        (4.7, '1984'),
        (4.5, 'The Great Gatsby')
    ]
    cursor.execute(new_col)
    cursor.executemany('update books set rating = ? where title = ?', ratings)
    
    print(cursor.execute('Select * from books order by year_published asc').fetchall())


