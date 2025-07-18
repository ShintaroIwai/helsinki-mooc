# Write your solution here
from random import choice
from string import ascii_lowercase, digits

def generate_strong_password(length: int, number: bool, special_char: bool):
    special_char_string = "!?=+-()#"
    char_list = []
    # add everything to one big list that the program will draw from
    for char in ascii_lowercase:
        char_list.append(char)
    for digit in digits:
        char_list.append(digit)
    for char in special_char_string:
        char_list.append(char)
    # Define condition and do a while loop based on condition
    while True:
        password = ""
        has_lowercase = False
        has_number = False
        has_special_char = False
        for i in range(length):
            char = choice(char_list)
            if char in ascii_lowercase:
                has_lowercase = True
            if char in digits:
                has_number = True
            if char in special_char_string:
                has_special_char = True
            password += char
        
        # take into account boolean input and return accordingly
        if not has_lowercase:
            continue
        if number and not has_number:
            continue
        if not number and has_number:
            continue
        if special_char and not has_special_char:
            continue
        if not special_char and has_special_char:
            continue
        break
        # if number and special_char:
        #     if has_lowercase and has_number and has_special_char:
        #         break
        # elif number and not special_char:
        #     if has_lowercase and has_number and not has_special_char:
        #         break
        # elif not number and special_char:
        #     if has_lowercase and not has_number and has_special_char:
        #         break
        # else:
        #     if has_lowercase and not(has_number or has_special_char):
        #         break
    
    return password

if __name__ == "__main__":
    print(generate_strong_password(3, True, True))