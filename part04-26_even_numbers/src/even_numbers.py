# Write your solution here
def even_numbers(my_list):
    new_list = []
    for number in my_list:
        if number % 2 == 0:
            new_list.append(number)
    return new_list

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)