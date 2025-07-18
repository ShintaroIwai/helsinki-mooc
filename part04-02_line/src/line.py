# Write your solution here
def line(integer: int, string: str):
    """Type in an integer and string"""
    if len(string) > 0:
        first_char = string[0]
    else:
        first_char = "*"
    print(first_char * integer)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")
    line(5, "xxx")
    line(3, "")