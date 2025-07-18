# Write your solution here
from string import ascii_lowercase, ascii_uppercase, printable, punctuation

def change_case(orig_string: str):
    new_string = ""
    for char in orig_string:
        if char in ascii_lowercase:
            new_char = char.upper()
        elif char in ascii_uppercase:
            new_char = char.lower()
        else:
            new_char = char
        new_string += new_char
    return new_string

def split_in_half(orig_string: str):
    # return orig_string[:len(orig_string) // 2], orig_string[len(orig_string) // 2:]
    # split_at = len(orig_string) // 2 - 1 # subtract 1 because of how indexes in Python work
    split_at = len(orig_string) // 2
    first_half = orig_string[:split_at]
    second_half = orig_string[split_at:]
    # first_half = ""
    # second_half = ""
    # for i in range(len(orig_string)):
    #     current_char = orig_string[i]
    #     if i <= split_at:
    #         first_half += current_char
    #     else:
    #         second_half += current_char
    return (first_half, second_half)

def remove_special_characters(orig_string: str):
    new_string = ""
    for char in orig_string:
        if char in printable and char not in punctuation:
            new_string += char
        else:
            continue
    return new_string

if __name__ == "__main__":
    my_string = "Well hello there!"

    print(change_case(my_string))

    p1, p2 = split_in_half(my_string)

    print(p1)
    print(p2)

    m2 = remove_special_characters("This is a test, lets see how it goes!!!11!")
    print(m2)