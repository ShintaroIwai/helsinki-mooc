# Write your solution here

# tuple contains name, age, and height
def store_personal_data(person: tuple):
    line = f"{person[0]};{person[1]};{person[2]}"
    with open("people.csv", "a") as new_file:
        new_file.write(line + "\n")

if __name__ == "__main__":
    store_personal_data(("Paul Paulson", 37, 175.5))