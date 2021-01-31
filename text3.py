# Text 3 // Web scraping from open-source .txt HTML pages

# Time period: 1465 

import requests

target_url = 'https://www.gutenberg.org/files/35461/35461-0.txt'

req = requests.get(target_url)

if req.status_code == 200:
    first_character = 420543
    characters_to_print = 507
    print("By this time, people had gained their own land in the middle of Eurasia.", end = "")
    print(req.text[first_character:first_character + characters_to_print])
else:
    print ("something went wrong, response code %i") % req.status_code
