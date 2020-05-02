fname = input("Enter the file name here >> ")

count = 0

try:
    fhand = open(fname)
    for line in fhand:
        count = count + 1
    print("There were", count, "subject lines in", fname)
except:
    if fname == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd")
    else:
        print("File cannot be opened:", fname)
