fname = input("Enter the file name here >> ")
fhand = open(fname)
emails = []
for line in fhand:
    if line.startswith("From "):
        words = line.split()
        emails.append(words[1])
print(emails)
print("There was", len(emails), "lines in the file with From as the first word")
