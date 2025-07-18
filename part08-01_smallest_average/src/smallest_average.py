# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict):
    lowest_average = 10
    lowest_dict = {}
    contestants = [person1, person2, person3]
    for person in contestants:
        average = (person["result1"] + person["result2"] + person["result3"]) / 3
        if average < lowest_average:
            lowest_dict = person
            lowest_average = average
    return lowest_dict

if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    print(smallest_average(person1, person2, person3))

    person4 = {"name": "Ana", "result1": 1,"result2": 1,"result3": 1}
    person5 = {"name": "Ana", "result1": 2,"result2": 2,"result3": 2}
    person6 = {"name": "Ana", "result1": 3,"result2": 3,"result3": 3}
    print(smallest_average(person4, person5, person6))