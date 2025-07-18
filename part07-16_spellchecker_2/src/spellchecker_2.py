# Write your solution here
def spell_checker():
    word_list = words_to_check()
    spellchecked = display_misspelled(word_list)
    print(spellchecked)
    misspelled = find_misspelled(word_list)
    suggestions = create_suggestions(misspelled)
    for key in suggestions:
        string = f"{key}: "
        suggestion_list = suggestions[key]
        for word in suggestion_list:
            if word == suggestion_list[len(suggestion_list) - 1]:
                string += f"{word}"
            else:
                string += f"{word}, "
        print(string)

def create_suggestions(misspelled: list):
    from difflib import get_close_matches
    english_words = open_file()
    suggestions = {}
    for word in misspelled:
        close_matches = get_close_matches(word, english_words)
        suggestions[word] = close_matches
    return suggestions

def display_misspelled(word_list: list):
    english_words = open_file()
    s = ""
    for item in word_list:
        word = item.lower()
        if word in english_words:
            if item == word_list[len(word_list) - 1]:
                s += item
            else:
                s += item + " "
        else:
            s += f"*{item}* "
    return s

def find_misspelled(word_list: list):
    english_words = open_file()
    misspelled = []
    for item in word_list:
        word = item.lower()
        if word not in english_words:
            misspelled.append(word)
    return misspelled

def open_file():
    english_words = []
    with open("src/wordlist.txt") as my_file:
        for line in my_file:
            line = line.strip()
            english_words.append(line)
    return english_words

def words_to_check():
    sentence = input("write text: ")
    words_to_check = sentence.split()
    return words_to_check

spell_checker()