# Exercise 1 for 5.1
# use try and except for non-number values
# now print out max and min numbers

count = 0
total = 0
maxvalue = None
minvalue = None
inputvalue = input("Enter a value: ")

while True:
    try:
        if inputvalue == "done":
            break
        else:
            total = total + int(inputvalue)
            count = count + 1
            if maxvalue is None:
                maxvalue = int(inputvalue)
                minvalue = int(inputvalue)
            elif maxvalue < int(inputvalue):
                maxvalue = int(inputvalue)
            elif minvalue > int(inputvalue):
                minvalue = int(inputvalue)
            inputvalue = input("Enter a value: ")
    except:
        print("Invalid input")
        inputvalue = input("Enter a value: ")

print("Total",total, "Count",count,"MinValue", minvalue,"MaxValue", maxvalue)
