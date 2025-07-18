# Copy here code of line function from previous exercise and use it in your solution
def line(integer: int, string: str):
    """Type in an integer and string"""
    if len(string) > 0:
        first_char = string[0]
    else:
        first_char = "*"
    print(first_char * integer)

def shape (size, tri_char, rect_height, rect_char):
    i = 1
    j = 1
    while i <= size:
        line(i, tri_char)
        i += 1
    while j <= rect_height:
        line(size, rect_char)
        j += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")