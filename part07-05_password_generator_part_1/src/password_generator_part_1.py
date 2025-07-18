# Write your solution here
def generate_password(number: int):
    from random import choice
    from string import ascii_lowercase
    password = ""
    for i in range(number):
        char = choice(ascii_lowercase)
        password += char
    return password

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))