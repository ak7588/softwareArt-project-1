# Text 2 // HTML parsing and the soup 🍜

# Time period: 400 BC

import requests
from bs4 import BeautifulSoup

things = ['cuisine', 'medicine', 'rock tools', 'coronavirus']
places = ['mountains', 'rocks', 'valleys', 'caves']

target_url = 'https://lyricstranslate.com/en/taboo-taboo.html-4'
req = requests.get(target_url)

# Checking for opening errors

if req.status_code != 200:
    print("something went wrong, response code %i" % req.status_code)

# Parsing

soup = BeautifulSoup(req.content, 'html.parser')
# title = soup.find('title')
lyrics = soup.find_all('div', class_ = 'par')
line = lyrics[12].text

print("Besides significant developments in %s, the following words were carved out on many %s:" % (random.choice(things), random.choice(places)))
print()
for char in range(205):
  print(line[char], end = '')
