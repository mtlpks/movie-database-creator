import mysql
import pandas as pd
import html_parsing
from tabulate import tabulate
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mla205766*"
)
cur = conn.cursor()
cur.execute("""DROP DATABASE IF EXISTS imdb_top_movies""")
cur.execute("""CREATE DATABASE imdb_top_movies""")
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mla205766*",
    database="imdb_top_movies"
)
curr = conn.cursor()
curr.execute("""CREATE TABLE directors
(id INT AUTO_INCREMENT PRIMARY KEY, director_name VARCHAR(50) NOT NULL UNIQUE)
""")
curr.execute(
"""CREATE TABLE movie_list
(movie_id INT AUTO_INCREMENT PRIMARY KEY, movie_rank INT, director_id INT, director_ph VARCHAR(55), title VARCHAR(55), year INT, INDEX fk_dir_id (director_id), FOREIGN KEY (director_id) REFERENCES directors(id))
""")
insert_movies = []
insert_director = []
insert_title = []
for key, value in html_parsing.movies_list.items():
    insert_movies.append((key, value[0], value[1], value[2]))
    insert_director.append((value[1],))
insert_movies_query = """INSERT INTO movie_list(movie_rank, title, director_ph, year) VALUES (%s, %s, %s, %s)"""
insert_director_query = """INSERT IGNORE INTO directors(director_name) VALUES (%s)"""
curr.executemany(insert_movies_query, insert_movies)
curr.executemany(insert_director_query, insert_director)
curr.execute("""UPDATE movie_list INNER JOIN directors ON movie_list.director_ph = directors.director_name SET movie_list.director_id = directors.id""")
df = pd.read_sql('SELECT movie_rank, title, year, directors.director_name FROM movie_list LEFT JOIN directors ON movie_list.director_id = directors.id', con=conn)
df.columns = ['Movie Rank', 'Title', 'Year','Director']
print(df.to_markdown())