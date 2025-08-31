# Write your solution here
def is_prime(number: int):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def prime_numbers():
    number = 2
    while True:
        if is_prime(number):
            yield number
        number += 1
            
if __name__ == "__main__":
    # print(is_prime(5))
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))
