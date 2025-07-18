# Write your solution here
def factorials(n: int):
    results = {}
    result = 1
    for i in range(1, n + 1):
        result *= i
        results[i] = result
    return results

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])