biglist = list()
biglist2 = list()
first_number = 231832
second_number = 767346
for intnumber in range(first_number, second_number):
    strnumber = str(intnumber)
    numberlist = list(strnumber)
    counts = dict()
    if numberlist == sorted(numberlist):
        for number in numberlist:
            counts[number] = counts.get(number, 0) + 1
        for key, value in counts.items():
            if value >= 2:
                if numberlist not in biglist:
                    biglist.append(numberlist)
            if value == 2:
                if numberlist not in biglist2:
                    biglist2.append(numberlist)

print("First problem:", len(biglist))
print("Second problem:", len(biglist2))
