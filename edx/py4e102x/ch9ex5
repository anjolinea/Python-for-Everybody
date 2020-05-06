fname = input("Enter file name >> " )
fhand = open(fname)

email_handles = dict()
for line in fhand:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        domainname = email.split("@")[1]
        email_handles[domainname] = email_handles.get(domainname, 0) + 1

print(email_handles)
