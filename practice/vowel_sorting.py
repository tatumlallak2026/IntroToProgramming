string = input("enter a string\n>")
num_vowels = 0
for letter in string:
    if letter in ["a", "e", "i", "o", "u"]:
        num_vowels += 1
print("there are " + str(num_vowels) + " vowels in the word " + string + ".")