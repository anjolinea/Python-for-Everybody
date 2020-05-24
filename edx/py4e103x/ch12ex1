import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
urlhostname = input("Enter the URL host name >> ")
while True:
    try:
        mysock.connect((urlhostname, 80))
        break
    except:
        print("Enter another URL")
        urlhostname = input("Enter the URL host name >> ")
componentparts = input("Enter the component part(s) >> ")
fullurl = "http://" + urlhostname + "/" + componentparts
cmd = 'GET ' + fullurl + ' HTTP/1.0\r\n\r\n'
cmd1 = cmd.encode()
mysock.send(cmd1)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()
