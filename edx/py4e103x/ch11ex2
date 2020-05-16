import re

numlist = list()
count = 0
hand = open("mbox-short.txt")
for line in hand:
    numbers = re.findall("^New Revision: ([0-9]+)", line)
    for number in numbers:
        number = float(number)
        numlist.append(number)
        count += 1

print(int(sum(numlist)/count))
