# write your solution here
if True:
    #this is never executed when False
    student_info = input("Student information: ")
    exercise_data = input("Exercise completed: ")
# else:
#     # hard-coded input, remove when program is complete
#     student_info = "src/students1.csv"
#     exercise_data = "src/exercises1.csv"

# making two helper dictionaries
names = {}
grades = {}
total_grade_dict = {}

# making a dictionary with names as keys and a tuple of first name and last name as value
with open(student_info) as new_file:
    for line in new_file:
        parts = line.split(";")
        id_number = parts[0]
        if id_number == "id":
            continue
        else:
            names[id_number] = (parts[1], parts[2].strip())

# making a dictionary with names as keys and a list of grades as the value
with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(";")
        id_number = parts[0]
        if id_number == "id":
            continue
        else:
            student_grades = []
            total_grade = 0
            for number in parts[1:]:
                student_grades.append(int(number))
                total_grade += int(number)
            grades[id_number] = student_grades
            total_grade_dict[id_number] = total_grade

for student, name in names.items():
    if student in total_grade_dict:
        total_grade = total_grade_dict[student]
        student_name = name[0] + " " + name[1]
        print(f"{student_name} {total_grade}")
    else:
        print("There is no student with that name!")





