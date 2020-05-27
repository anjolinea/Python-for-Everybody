import json
from urllib.request import urlopen
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Connect to URL, get back data and convert to string
url = input("Enter location- ")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_531743.json"
print("Retrieving", url)
data = urlopen(url, context=ctx).read()
data_string = data.decode()

#Make JSON dictionary
info = json.loads(data_string)

#Retrieve tag with "count"
count = 0
lst = info["comments"]
for item in lst:
    count = count + int(item.get("count"))
print(count)
