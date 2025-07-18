# Write your solution here
def no_shouting(my_list : list):
    new_list = []
    for string in my_list:
        isitupper = string.isupper()
        if isitupper == False:
            new_list.append(string)
    return new_list

# Testing the function
if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)