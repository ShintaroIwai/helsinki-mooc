# Write your solution here
def most_common_character(my_string : str):
    most_common_count = 0
    most_common_char = ""
    for char in my_string:
        count = my_string.count(char)
        if count > most_common_count:
            most_common_count = count
            most_common_char = char
    return most_common_char

if __name__ == "__main__":
    first_string = "abcdbde" 
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))
