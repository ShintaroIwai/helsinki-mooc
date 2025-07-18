# Write your solution here
def print_persons(filename: str):
    import json
    with open(filename) as new_file:
        data = new_file.read()
        courses = json.loads(data)
        for row in courses:
            name = row["name"]
            age = row["age"]
            # hobbies = row["hobbies"]
            # hobbies_str = ""
            hobbies = ", ".join(row["hobbies"])
            # for i in range(len(hobbies)):
            #     hobby = hobbies[i]
            #     hobbies_str += hobby
            #     if i < len(hobbies) - 1:
            #         hobbies_str += ", "
            #     else:
            #         continue
            print(f"{name} {age} years ({hobbies})")

if __name__ == "__main__":
    print_persons("src/file1.json")