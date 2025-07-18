# Write your solution here
def length_of_longest(my_list : list):
    longest_word = ""
    for word in my_list:
        if len(word) > len(longest_word):
            longest_word = word
    return len(longest_word)

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = length_of_longest(my_list)
    print(result)