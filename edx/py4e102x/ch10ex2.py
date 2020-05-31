fname = input("Enter file name>> ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fhand = open(fname)

hours_dict = dict()
for line in fhand:
    if line.startswith("From "):
        words = line.split()
        hour = words[5].split(":")[0]
        hours_dict[hour] = hours_dict.get(hour, 0) + 1

for hours_address, hours_count in sorted(hours_dict.items()):
    print(hours_address, hours_count)
