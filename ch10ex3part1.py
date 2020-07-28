#only works if you directly enter the strings in, not if you open a file
fhand = "But soft what light through yonder window breaks" \
        "Romeo wack"
letter_dict = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        letters = word.split()
        for letter in letters:
            letter = letter.lower()
            if letter.isalpha() is True:
                letter_dict[letter] = letter_dict.get(letter, 0) + 1

reverse_letter_list = list()
for letter_address, letter_value in letter_dict.items():
    reverse_letter_list.append((letter_value, letter_address))

sorted_reverse_letter_list = sorted(reverse_letter_list, reverse=True)
for key, value in sorted_reverse_letter_list:
    print(value, key)
