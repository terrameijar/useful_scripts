#! /usr/bin/env python
# lucky.py -- Opens several Google search results.

import sys
import requests
import webbrowser
from bs4 import BeautifulSoup

print "Googling....."   # Display text while searching
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = BeautifulSoup(res.text, "lxml")

# Open a browser tab for each result.
link_elements = soup.select('.r a')  # Select anchor under class r
num_open = min(5, len(link_elements))
for i in range(num_open + 1):
    webbrowser.open('http://google.com' + link_elements[i].get('href'))