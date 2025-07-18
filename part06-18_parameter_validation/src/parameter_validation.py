# Write your solution here
def new_person(name: str, age: int):
    if name == "":
        raise ValueError("The name is empty!")
    elif " " not in name:
        raise ValueError("The name should contain more than one word!")
    elif len(name) > 40:
        raise ValueError("The name is too long!")
    elif age < 0 or age > 150:
        raise ValueError("This is not a valid age: " + str(age))
    else:
        return (name, age)

