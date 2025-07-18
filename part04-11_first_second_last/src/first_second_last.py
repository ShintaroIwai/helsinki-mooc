# Write your solution here
def first_word(sentence):
    index = 0
    while index <= len(sentence):
        if sentence[index] == " ":
            return sentence[0:index]
        if index == len(sentence) - 1:
            return sentence[0:index + 1]
        index += 1

def second_word(sentence):
    new_sentence = sentence.replace(first_word(sentence), "")
    new_sentence2 = new_sentence[1:]
    return first_word(new_sentence2)

def last_word(sentence):
    index = -1
    while -index <= len(sentence):
        if sentence[index] == " ":
            return sentence[index + 1:]
        index -= 1 

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))