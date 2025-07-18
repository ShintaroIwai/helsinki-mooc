# Write your solution here
def everything_reversed(my_list : list):
    new_list = []
    index = -1
    while -index <= len(my_list):
        word = my_list[index]
        reversed_word = word[::-1]
        new_list.append(reversed_word)
        index -= 1
    return new_list

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)