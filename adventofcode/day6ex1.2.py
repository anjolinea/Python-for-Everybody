from itertools import combinations

#Only works for the sample code

big_list = list()
big_list_1 = list()
big_list_2 = list()
big_list_3 = list()
f_hand = open("adventday6.txt")

# list of pairs [[COM, B],[B,C]...]
for line in f_hand:
    temp_lst = (line.rstrip().split(")"))
    big_list.append(temp_lst)

for temp_list in big_list:
    big_list_1.append(temp_list)
    big_list_2.append(temp_list)

# Find beginning(s) ["COM"]
for temp1 in big_list:
    for temp in big_list_2:
        if temp[0] == temp1[1]:
            big_list_2.remove(temp)
for temp_list_1 in big_list_2:
    big_list_2.append(temp_list_1[0])
    big_list_2.remove(temp_list_1)

# Find ends
for small_list_ in big_list:
    for small_list_0 in big_list_1:
        if small_list_0[1] == small_list_[0]:
            big_list_1.remove(small_list_0)

# big_list_1 has the pairs that need to be stretched
# big_list has all of them
# Start of loop
while True:
    for small_list_1 in big_list_1:
        for small_list in big_list:
            if len(small_list) == 2:
                if small_list_1[0] == small_list[1]:
                    small_list_1.insert(0, small_list[0])
                    for element in big_list:
                        if len(element) > 2:
                            big_list.remove(element)
        for beginning in big_list_2:
            if small_list_1[0] == beginning:
                big_list_3.append(small_list_1)
                big_list_1.remove(small_list_1)
    if len(big_list_1) == 0:
        print("break")
        break

big_list_3 = sorted(big_list_3, key=len, reverse=True)
big_list_4 = list()

for small_list_3 in big_list_3:
    comb = combinations(small_list_3, 2)
    for combination in list(comb):
        if combination not in big_list_4:
            big_list_4.append(combination)
print(len(big_list_4))
