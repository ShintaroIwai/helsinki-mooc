# Write your solution here
def longest(strings: list):
    longest_string = ""
    for word in strings:
        if len(word) > len(longest_string):
            longest_string = word
            
    return longest_string

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))