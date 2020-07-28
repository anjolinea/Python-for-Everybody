import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
urlhostname = input("Enter the URL host name >> ")
if len(urlhostname) < 1:
    urlhostname = "data.pr4e.org"
while True:
    try:
        mysock.connect((urlhostname, 80))
        break
    except:
        print("Enter another URL")
        urlhostname = input("Enter the URL host name >> ")
componentparts = input("Enter the component part(s) >> ")
if len(componentparts) < 1:
    componentparts = "intro-short.txt"
fullurl = "http://" + urlhostname + "/" + componentparts
cmd = 'GET ' + fullurl + ' HTTP/1.0\r\n\r\n'
cmd1 = cmd.encode()
mysock.send(cmd1)


data = mysock.recv(3000)
print(data.decode(), end='')
print("\nlength", len(data))

mysock.close()
