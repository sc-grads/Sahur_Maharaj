import requests
from bs4 import BeautifulSoup


url = 'https://www.python.org'
page = requests.get(url)
print(type(page))

print(page.status_code)
print(page.ok)

print(page.content)  # <-- as bytes
print(page.content.decode())
print(page.text)  # <-- unicode

print(page.headers)

# beautiful soup

soup = BeautifulSoup(page.text, 'html.parser')
print(soup.title)
print(soup.body)
print(soup.find('p'))  # find_all['div', 'p']
print(soup.find('p').text)
for t in soup.find_all('p'):
    print(t.text)

