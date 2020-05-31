# using ch9ex4
# use dictionaries to not print a tuple?

fname = input("Enter file name>> ")
fhand = open(fname)

emails = dict()
for line in fhand:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        emails[email] = emails.get(email, 0) + 1

reverse_email = list()
for email_address, email_count in emails.items():
    reverse_email.append((email_count, email_address))

print(sorted(reverse_email, reverse=True)[0])
