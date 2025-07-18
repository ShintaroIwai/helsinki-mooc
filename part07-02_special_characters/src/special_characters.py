# Write your solution here
def separate_characters(my_string: str):
    import string

    ascii_string = ""
    punctuation_string = ""
    others = ""
    for char in my_string:
        if char in string.ascii_letters:
            ascii_string += char
        elif char in string.punctuation:
            punctuation_string += char
        else:
            others += char
    
    separated = (ascii_string, punctuation_string, others)

    return separated

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])