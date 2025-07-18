# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
def palindromes(my_string : str):
    reversed_string = ""
    original_string = my_string
    while len(my_string) > 0:
        reversed_string += my_string[-1]
        my_string = my_string[0:-1]
    return original_string == reversed_string

# Main program
while True:
    string = input("Please type in a palindrome: ")
    if palindromes(string) == True:
        print(f"{string} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")
