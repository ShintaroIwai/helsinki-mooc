# Write your solution here
def all_the_longest(my_list : list):
    length_list = []
    new_list = []
    
    for word in my_list:
        length_list.append(len(word))
        max_length = max(length_list)

    for word in my_list:
        if len(word) == max_length:
            new_list.append(word)

    return new_list

# Testing
if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)
    print(result) # ['eleventh']

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']