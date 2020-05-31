biglist = list()
first_number = int(input("Enter the first number of the range >> "))
second_number = int(input("Enter the second number of the range >> "))
for intnumber in range(first_number, second_number):
    strnumber = str(intnumber)
    numberlist = list(strnumber)
    for start_number in range(0,5):
        if numberlist[start_number] == numberlist[start_number + 1]:
                if numberlist == sorted(numberlist):
                    if numberlist not in biglist:
                        biglist.append(numberlist)

print("First problem:", len(biglist))
