fname = input("Enter file name>> " )
fhand = open(fname)

emails = dict()
for line in fhand:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        emails[email] = emails.get(email, 0) + 1

big_count = None
big_email = None

for email_address, email_count in emails.items():
    if big_count is None or email_count > big_count:
        big_count = email_count
        big_email = email_address

print(big_email, big_count)
