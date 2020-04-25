#Exercise 1 for 5.1
#use try and except for non-number values

count = 0
total = 0
inputvalue = input("Enter a value: ")

while True:
    try:
        if inputvalue == "done":
            average = total / count
            print(total, count, average)
            break
        else:
            total = total + int(inputvalue)
            count = count + 1
            inputvalue = input("Enter a value: ")
    except:
        print("Invalid value")
        inputvalue = input("Enter a value: ")
