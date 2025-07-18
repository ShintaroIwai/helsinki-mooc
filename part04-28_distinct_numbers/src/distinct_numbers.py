# Write your solution here
def distinct_numbers(my_list : list):
    new_list = []
    sorted_list = sorted(my_list)
    for number in sorted_list:
        if new_list == [] or number != new_list[-1]:
            new_list.append(number)
    new_list_sorted = sorted(new_list)
    return new_list_sorted

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]