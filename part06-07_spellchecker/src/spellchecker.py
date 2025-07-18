# write your solution here
word_list = []

# Open the text file and put all words in a list
with open("src/wordlist.txt") as new_file:
    for line in new_file:
        new_line = line.strip()
        word_list.append(new_line)

# Make a list of all the words in the input
sentence = input("Write text: ")
words = sentence.split(" ")

# Check words in the list against the word list
for i in range(len(words)):
    if words[i].lower() not in word_list:
        words[i] = "*" + words[i] + "*"

# Finally print the sentence
spellchecked = ""
for i in range(len(words)):
    if i != len(words) - 1:
        spellchecked += words[i] + " "
    else:
        spellchecked += words[i]
print(spellchecked)
