# Write your solution here
def words(n: int, beginning: str):
    from random import sample
    # list of all the words in the words.txt file
    words = []
    # list of all words eligible to pick from
    word_list = []
    with open("src/words.txt") as new_file:
        for line in new_file:
            line = line.strip()
            words.append(line)
        for word in words:
            match = True
            if len(beginning) > len(word):
                match = False
            else:
                for i in range(len(beginning)):
                    if beginning[i] == word[i]:
                        continue
                    else:
                        match = False
                        break
                if match:
                    word_list.append(word)
        # word.startswith(beginning)
    
    # pick n entries out of word_list
    if len(word_list) < n:
        raise ValueError(str("n") + " was larger than the number of words eligible!")
    else:
        chosen = sample(word_list, n)
        return chosen

if __name__ == "__main__":
    word_list = words(2, "car")
    for word in word_list:
        print(word)