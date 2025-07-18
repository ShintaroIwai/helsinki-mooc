# Write your solution here
def histogram(string: str):
    count = {}
    for char in string:
        # if the character is not yet in the dictionary, initialize the value to zero
        if char not in count:
            count[char] = 0
        # increment the value
        count[char] += 1

    for char in count:
        print(f"{char}", "*" * count[char])

if __name__ == "__main__":
    histogram("abba")
    histogram("statistically")