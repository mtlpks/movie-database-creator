import sqlite3
import pandas as pd
import html_parsing
from tabulate import tabulate
conn = sqlite3.connect('movie_list')
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS movie_list
([movie_id] SERIAL PRIMARY KEY, [movie_rank] INTEGER, [director] TEXT, [rating] REAL, [year] INTEGER)
''')
for key, value in html_parsing.movies_list.items():
    cur.execute('''
    INSERT INTO movie_list(movie_rank, director, rating, year) 
    VALUES(?, ?, ?, ?)
    ''',(key, value[0], value[1], value[2]))
cur.execute('''
            SELECT
            movie_rank, 
            director, 
            rating, 
            year 
            FROM movie_list''')
df = pd.DataFrame(cur.fetchall(), columns=['movie_rank', 'director', 'rating', 'year'])
print(tabulate(df, headers= 'keys', tablefmt= 'psql'))