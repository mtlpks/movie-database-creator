import requests
from bs4 import BeautifulSoup
import re
page = requests.get(url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250").text
soup = BeautifulSoup(page, 'html.parser')
title_column = soup.find_all(class_="titleColumn")
list_of_htmlsections = []
for element in title_column:
    list_of_htmlsections.append(str(element))
movies_list = {}
ranking_number = 1
for movie_number in range(0, len(list_of_htmlsections)):
    director_re = re.findall(r'/" title=".+?dir.', list_of_htmlsections[movie_number])
    director = director_re[0][10:-6]
    movie_name_re = re.findall(r'>.*?</a>', list_of_htmlsections[movie_number])
    movie_name = movie_name_re[0][1:-4]
    year_re = re.findall(r">.*?</s", list_of_htmlsections[movie_number])
    year = year_re[0][2:-4]
    movies_list[ranking_number] = [movie_name, director, year]
    ranking_number += 1