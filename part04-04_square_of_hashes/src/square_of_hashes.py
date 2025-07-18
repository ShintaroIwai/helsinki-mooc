# Copy here code of line function from previous exercise
def line(integer: int, string: str):
    """Type in an integer and string"""
    if len(string) > 0:
        first_char = string[0]
    else:
        first_char = "*"
    print(first_char * integer)

def square_of_hashes(size):
    # You should call function line here with proper parameters
    index = 0
    while index < size:
        line(size, "#")
        index += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
