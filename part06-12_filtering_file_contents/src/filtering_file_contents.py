# Write your solution here
def read_files():
    student_answers = []
    with open("src/solutions.csv") as new_file:
        for line in new_file:
            line = line.strip()
            line = line.split(";")
            student_answers.append(line)
    return student_answers

def correct_or_incorrect(student_answers: list):
    for row in student_answers:
        row[2] = int(row[2])
        problem = eval(row[1])
        answer = row[2]
        if problem == answer:
            row.append("correct")
        else:
            row.append("incorrect")
    return student_answers

def write_the_file(student_answers: list):
    # clean the files first since the file needs to be the same even if you run it multiple times in a row
    with open("correct.csv", "w") as new_file:
        pass
    with open("incorrect.csv", "w") as new_file:
        pass
    # finally writing to the files
    for row in student_answers:
        if row[3] == "correct":
            with open("correct.csv", "a") as new_file:
                line = f"{row[0]};{row[1]};{row[2]}"
                new_file.write(line+"\n")
                # line = ""
                # for i in range(len(row) - 1):
                #     item = row[i]
                #     line += f"{item};"
                # new_file.write(line+"\n")
        if row[3] == "incorrect":
            with open("incorrect.csv", "a") as new_file:
                line = f"{row[0]};{row[1]};{row[2]}"
                new_file.write(line+"\n")
                # line = ""
                # for i in range(len(row) - 1):
                #     item = row[i]
                #     line += f"{item};"
                # new_file.write(line+"\n")

def filter_solutions():
    student_data = read_files()
    filtered_data = correct_or_incorrect(student_data)
    write_the_file(filtered_data)

if __name__ == "__main__":
    filter_solutions()
