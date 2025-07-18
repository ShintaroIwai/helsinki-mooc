# WRITE YOUR SOLUTION HERE:
from string import punctuation

def most_common_words(filename: str, lower_limit: int):
    with open(filename) as new_file:
        lines = [line.replace("\n", "").split() for line in new_file]
        words = [item.strip(punctuation) for sentence in lines for item in sentence]
        return {word : words.count(word) for word in words if words.count(word) >= lower_limit}

    # words = []
    # with open(filename) as new_file:
    #     for line in new_file:
    #         line = line.replace("\n", "")
    #         line = line.split()
    #         for word in line:
    #             words.append(word)
    # return words

if __name__ == "__main__":
    print(most_common_words("comprehensions.txt", 3))
