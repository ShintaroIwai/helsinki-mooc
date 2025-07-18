# Write your solution here
def no_vowels(string : str):
    vowels = "aeiouAEIOU"
    for char in string:
        if char in vowels:
            string = string.replace(char, "")
    return string

# Testing the function
if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))