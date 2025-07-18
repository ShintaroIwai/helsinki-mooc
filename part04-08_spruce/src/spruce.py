# Write your solution here
def spruce(size):
    print("a spruce!")
    """Size specifies how big the tree will be"""
    row = 1
    while size > 0:
        space = " " * (size - 1)
        tree = "*" * (row * 2 - 1)
        print(space + tree + space)
        size -= 1
        row += 1
    print(" " * (row - 2) + "*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)