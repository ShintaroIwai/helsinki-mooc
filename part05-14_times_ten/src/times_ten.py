# Write your solution here
def times_ten(start_index: int, end_index: int):
    results = {}
    for number in range(start_index, end_index + 1):
        results[number] = number * 10
    return results

if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)