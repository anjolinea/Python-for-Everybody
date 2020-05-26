import xml.etree.ElementTree as ET
from urllib.request import urlopen
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Connect to URL, get back data and convert to string
url = input("Enter location- ")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_531742.xml"
print("Retrieving", url)
data = urlopen(url, context=ctx).read()
data_string = data.decode()

#Make element tree and make list for comment tags
tree = ET.fromstring(data_string)
lst = tree.findall("comments/comment")

count = 0
for item in lst:
    count = count + int(item.find("count").text)
print("Count", len(lst))
print("Sum", count)
