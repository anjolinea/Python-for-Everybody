fname = input("Enter file name>> " )
fhand = open(fname)

emails = dict()
for line in fhand:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        emails[email] = emails.get(email, 0) + 1

print(emails)
