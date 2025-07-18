# Write your solution here
def lottery_numbers(amount: int, lower: int, upper: int):
    from random import randint
    number_list = []
    while len(number_list) < amount:
        random_number = randint(lower, upper)
        if random_number not in number_list:
            number_list.append(random_number)
    number_list.sort()
    return number_list

if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)