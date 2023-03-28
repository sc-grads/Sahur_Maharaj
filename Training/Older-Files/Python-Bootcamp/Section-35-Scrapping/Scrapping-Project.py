import requests
from bs4 import BeautifulSoup as bs
import openpyxl

url = ('https://www.imdb.com/search/title?release_date=2019-01-01,2019-12-31&sortnum_votes,desc&ref=adv_prv')
page = requests.get(url)
soup = bs(page.content, 'html.parser')
content = soup.find_all('div', class_='lister-item-content')

movies = []
for i in content:
    name = i.h3.a.text
    rating = i.strong.text
    movies.append((name, rating))

print(movies)

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'IMDB MOVIES'
sheet['a1'] = 'Year'
sheet['b1'] = 'Rating'

for m in movies:
    sheet.append(m)
wb.save('Movies2019.xlsx')