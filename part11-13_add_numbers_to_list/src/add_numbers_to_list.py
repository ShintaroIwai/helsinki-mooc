# WRITE YOUR SOLUTION HERE:
def add_numbers_to_list(numbers: list):
    if len(numbers) % 5 != 0:
        # append number one greater than the last number in the list
        numbers.append(numbers[-1] + 1)
        add_numbers_to_list(numbers)

if __name__ == "__main__":
    my_list = [1,3]
    add_numbers_to_list(my_list)
    print(my_list)

    numbers = [1,3,4,5,10,11]
    add_numbers_to_list(numbers)
    print(numbers)
