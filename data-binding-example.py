#binds data from youtube homepage

import urllib.request
from bs4 import BeautifulSoup

url = "http://www.youtube.com/"
getSource = urllib.request.urlopen(url)
soup = BeautifulSoup(getSource, 'html.parser')

content = soup.find_all('h3', attrs={'class': 'yt-lockup-title'})

for i in range(0, len(content)):
    print(i, ")", content[i].text)
