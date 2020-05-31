fhand = open("romeo.txt")
unique_words = []
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
print(sorted(unique_words))
