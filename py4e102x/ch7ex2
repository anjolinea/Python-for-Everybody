fname = input("Enter the file name here >> ")
fhand = open(fname)

bigboi = 0
count = 0

for line in fhand:
    if line.startswith("X-DSPAM-Confidence: "):
        number = line[20:]
        number = number.rstrip()
        number = float(number)
        bigboi = bigboi + number
        count = count + 1

average = bigboi/count
print("Average spam confidence:", average)
