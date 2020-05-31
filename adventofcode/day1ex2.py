fuel = open("adventofcode2019day1.txt")

total = 0

for mass in fuel:
    mass = mass.rstrip()
    mass = int(mass)
    while True:
        something = int(mass/3)-2
        total = total + something
        if something >= 6:
            mass = something
            continue
        else:
            break
print(total)
