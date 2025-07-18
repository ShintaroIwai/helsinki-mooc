# write your solution here
def read_fruits():
    with open("src/fruits.csv") as new_file:
        fruit_dict = {}
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            fruit = parts[0]
            price = float(parts[1])
            fruit_dict[fruit] = price
    return(fruit_dict)

if __name__ == "__main__":
    dictionary = read_fruits()
    print(dictionary)