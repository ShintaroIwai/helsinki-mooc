# Write your solution here
def dictionary():
    while True:
        print("1 - Add word, 2 - Search, 3 - Quit")
        number = int(input("Function: "))
        if number == 1:
            suomi = input("The word in Finnish: ")
            english = input("The word in English: ")
            add_word(suomi, english)
        if number == 2:
            search_term = input("Search term: ")
            search(search_term)
        if number == 3:
            break
    print("Bye!")

def add_word(suomi: str, english: str):
    with open("src/dictionary.txt", "a") as new_file:
        new_file.write(f"{suomi};{english}\n")
    # need to add new entries to dictionary.txt
    print("Dictionary entry added")

def search(search_term: str):

    with open("src/dictionary.txt", "r") as new_file:
        for line in new_file:
            line = line.strip()
            pair = line.split(";")

            for word in pair:
                if search_term in word:
                    print(f"{pair[0]} - {pair[1]}")

dictionary()
# search("bag")
# add_word("auto", "car")
# add_word("laukku", "bag")