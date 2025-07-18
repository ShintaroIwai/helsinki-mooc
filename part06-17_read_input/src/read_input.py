# Write your solution here
def read_input(prompt: str, number1: int, number2: int):
    while True:
        try:
            number = int(input(prompt))
            if number > number1 and number < number2:
                return number
        except ValueError:
            pass

        print(f"You must type in an integer between {number1} and {number2}")

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)
