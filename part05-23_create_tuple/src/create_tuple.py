# Write your solution here
def create_tuple(x: int, y: int, z: int):
    # first is smallest, second is the greatest, third is the sum of the three arguments
    new_tuple = (min(x, y, z), max(x, y, z), x + y + z)
    return new_tuple

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))