#Only works for the sample code
biglist = list()
biggerlist = list()
count = 0
fhand = open("adventday6.txt")
for line in fhand:
    templst = (line.rstrip().split(")"))
    tempdict = dict()
    tempdict[templst[0]] = templst[1]
    biglist.append(tempdict)

for smalldict in biglist:
    for key, value in smalldict.items():
        for smalldict1 in biglist:
            for key1, value1 in smalldict1.items():
                if key == value1:
                    biggerlist.append([value, key, key1])

for smalllist in biggerlist:
    for smalllist1 in biggerlist:
        if len(smalllist) == len(smalllist1):
            if smalllist[len(smalllist)-1] == smalllist1[len(smalllist1)-2]:
                anotherlist = list()
                for element_in_small_list in smalllist:
                    anotherlist.append(element_in_small_list)
                anotherlist.append(smalllist1[len(smalllist1)-1])
                if anotherlist not in biggerlist:
                    biggerlist.append(anotherlist)
                    print(len(biggerlist))

print(len(biggerlist)+len(biglist))
