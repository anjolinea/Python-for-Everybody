# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_531740.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

count = 0
tagsum = 0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # what's inside the html, not tags
    tagsum = tagsum + int(tag.contents[0])
    count = count + 1
print("Count", count)
print("Sum", tagsum)
