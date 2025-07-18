# Write your solution here
# defining a function to read the files
def read_word_list():
    word_list = []
    with open("src/words.txt") as new_file:
        for line in new_file:
            line = line.strip()
            word_list.append(line)
    return word_list

def find_words(search_term: str):
    result = []
    word_list = read_word_list()
    # exact match
    if search_term in word_list:
        result.append(search_term)

    # dealing with periods
    elif "." in search_term:
        for word in word_list:
            if len(word) == len(search_term):
                eligibility = False
                for i in range(len(word)):
                    # if the letter matches then flip eligibility to true
                    if word[i] == search_term[i] or search_term[i] == ".":
                        eligibility = True
                    else:
                        eligibility = False
                        break
                if eligibility == True:
                    result.append(word)
            else:
                continue

    # starting asterisk - use endswith
    elif search_term[0] == "*":
        end = search_term[1:]
        for word in word_list:
            eligibility = word.endswith(end)
            if eligibility == True:
                result.append(word)

    # ending asterisk - use startswith
    elif search_term[len(search_term) - 1] == "*":
        start = search_term[:-1]
        for word in word_list:
            eligibility = word.startswith(start)
            if eligibility == True:
                result.append(word)

    return result

if __name__ == "__main__":
    # test for starting asterisk
    print(find_words("*vokes"))
    # test for ending asterisk
    print(find_words("aard*"))
    # test for periods
    print(find_words("ca."))
    print(find_words(".a.e"))