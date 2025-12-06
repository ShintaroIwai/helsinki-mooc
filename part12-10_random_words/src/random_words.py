# Write your solution here:
from random import randint

def word_generator(characters: str, length: int, amount: int):
    number = 0
    while number < amount:
        yield random_string(characters, length)
        number += 1

def random_string(characters: str, length: int):
    number_list = []
    word = ""
    for i in range(length):
        number_list.append(randint(0, len(characters)))
    for j in number_list:
        word += characters[j-1]
    return word

if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)
