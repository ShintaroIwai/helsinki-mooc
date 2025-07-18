# Write your solution here
def shortest(my_list : list):
    shortest_word = my_list[0]
    for word in my_list:
        if len(word) < len(shortest_word):
            shortest_word = word
    return shortest_word

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result)

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)