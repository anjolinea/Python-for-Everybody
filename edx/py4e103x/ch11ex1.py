import re

count = 0
hand = open("mbox-short.txt")
regex = input("Enter a regular expression >> ")
for line in hand:
    regex_occurences = re.findall(regex, line)
    for occurence in regex_occurences:
        count += 1
print(count, regex)
