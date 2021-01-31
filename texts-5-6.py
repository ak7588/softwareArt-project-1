# Text 5 & 6 // Regular Expression + String manipulation

# Time period: 1922

import requests
from bs4 import BeautifulSoup

target_url = 'https://www.advantour.com/uzbekistan/history.htm#:~:text=Uzbekistan%20is%20located%20in%20the,most%20ancient%20in%20the%20world.'
req = requests.get(target_url)

# Checking for opening errors

if req.status_code != 200:
    print("something went wrong, response code %i" % req.status_code)

# Parsing

soup = BeautifulSoup(req.content, 'html.parser')
text = soup.find_all('p')

line_1 = text[0].text
line_2 = text[1].text

line_1 = line.replace('Uzbekistan', 'K*zakh-stan')
line_2 = line.replace('Uzbekistan', 'K*zakh-stan')

print("At this time, ", end = "")
print(line_1) # This is text 5
print()
print(line_2) # This is text 6
