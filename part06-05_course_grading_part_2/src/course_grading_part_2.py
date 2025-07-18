# wwite your solution here
if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")

# # delete after testing
# student_info = "src/students1.csv"
# exercise_data = "src/exercises1.csv"
# exam_data = "src/exam_points1.csv"

names = {}
exercise_points_dict = {}
total_exercise_points_dict = {}
exercise_grade_dict = {}
exam_points_dict = {}
final_points_dict = {}
final_grade_dict = {}

# making a dictionary with names as keys and a tuple of first name and last name as value
with open(student_info) as new_file:
    for line in new_file:
        parts = line.split(";")
        id_number = parts[0]
        if id_number == "id":
            continue
        else:
            names[id_number] = (parts[1], parts[2].strip())

# making a dictionary with names as keys and a list of exercise grades as the value
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
            # exercise grade is 10-19%: 1, 20%-29%: 2, 30%-39%: 3 and so on, so round down the division (40 total)
            exercise_grade = 10 * total_grade // 40
            exercise_points_dict[id_number] = student_grades
            total_exercise_points_dict[id_number] = total_grade
            exercise_grade_dict[id_number] = exercise_grade

# making a dictionary with names as keys and a list of exam grades as the value
with open(exam_data) as new_file:
    for line in new_file:
        parts = line.split(";")
        id_number = parts[0]
        if id_number == "id":
            continue
        else:
            total_exam_points = 0
            for number in parts[1:]:
                total_exam_points += int(number)
            exam_points_dict[id_number] = total_exam_points
    
# new dictionary that adds the exercise and exam points together
for name in names:
    final_points_dict[name] = exercise_grade_dict[name] + exam_points_dict[name]

# now classify the total final points according to the grade scale
for name in names:
    if final_points_dict[name] >= 28:
        final_grade_dict[name] = 5
    elif final_points_dict[name] >= 24:
        final_grade_dict[name] = 4
    elif final_points_dict[name] >= 21:
        final_grade_dict[name] = 3
    elif final_points_dict[name] >= 18:
        final_grade_dict[name] = 2
    elif final_points_dict[name] >= 15:
        final_grade_dict[name] = 1
    else:
        final_grade_dict[name] = 0

for student, name in names.items():
    if student in names:
        final_grade = final_grade_dict[student]
        student_name = name[0] + " " + name[1]
        print(f"{student_name} {final_grade}")
    else:
        print("There is no record of this student!")




