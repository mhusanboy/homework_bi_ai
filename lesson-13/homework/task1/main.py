import sqlite3
import os
from pathlib import Path

current_dir = Path(__file__).resolve().parent 


with sqlite3.connect(current_dir/'roster.db') as con:
    roster_table = """
        drop table if exists Roster;
        create table Roster(name text, species text, age int);
    """
    values = [
        ('Benjamin Sisko', 'Human', 40),
        ('Jadzia Dax', 'Trill', 300),
        ('Kira Nerys', 'Bajoran', 29)
    ]

    update_statement = """
        update Roster set name = 'Ezri Dax' where name = 'Jadzia Dax';
    """

    query_statement = """
        select name, age from Roster where species = 'Bajoran';
    """

    delete_statement = """
        Delete from Roster where age > 100;
    """
    add_column = """
        Alter table Roster add column Rank text;
    """

    ranks = [
        ('Captain','Benjamin Sisko'),
        ('Lieutenant','Ezri Dax'),
        ('Major','Kira Nerys')
    ]

    cursor = con.cursor()
    cursor.executescript(roster_table)
    cursor.executemany('Insert into Roster values(?, ?, ?)', values)
    cursor.execute(update_statement)
    data = cursor.execute(query_statement)
    print(data.fetchall())
    cursor.execute(delete_statement)
    cursor.execute(add_column)
    cursor.executemany('Update Roster set rank = ? where name = ?',ranks)
    data = cursor.execute('Select * from Roster order by age desc')
    print(data.fetchall())

