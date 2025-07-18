# tee ratkaisu tänne
if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
    course_info = input("Course information: ")

# # delete after testing
# student_info = "src/students1.csv"
# exercise_data = "src/exercises1.csv"
# exam_data = "src/exam_points1.csv"
# course_info = "src/course1.txt"

names = {}
exercise_points_dict = {}
total_exercise_points_dict = {}
exercise_grade_dict = {}
exam_points_dict = {}
final_points_dict = {}
final_grade_dict = {}
course_info_dict = {}

# making a dictionary with names as keys and a tuple of first name and last name as value
with open(student_info) as new_file:
    for line in new_file:
        parts = line.split(";")
        id_number = parts[0]
        if id_number == "id":
            continue
        else:
            names[id_number] = (parts[1], parts[2].strip())

with open(course_info) as new_file:
    for line in new_file:
        line = line.split(":")
        course_info_dict[line[0]] = line[1].strip()

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

def create_results_txt_file():
    with open("results.txt", "w") as new_file:
        heading = f"{course_info_dict["name"]}, {course_info_dict["study credits"]} credits" + "\n"
        new_file.write(heading)
        new_file.write(f"{"=" * (len(heading) - 1)}\n")
        new_file.write(f"{"name":30}{"exec_nbr":10}{"exec_pts.":10}{"exm_pts.":10}{"tot_pts.":10}{"grade":10}" + "\n")
        for idnumber, name in names.items():
            full_name = name[0] + " " + name[1]
            exec_number = total_exercise_points_dict[idnumber]
            exec_points = exercise_grade_dict[idnumber]
            exam_points = exam_points_dict[idnumber]
            total_points = final_points_dict[idnumber]
            final_grade = final_grade_dict[idnumber]
            new_file.write(f"{full_name:30}{exec_number:<10}{exec_points:<10}{exam_points:<10}{total_points:<10}{final_grade:<10}" + "\n")

def create_results_csv_file():
    with open("results.csv", "w") as new_file:
        for idnumber, name in names.items():
            full_name = name[0] + " " + name[1]
            final_grade = final_grade_dict[idnumber]
            new_file.write(f"{idnumber};{full_name};{final_grade}\n")

print("Results written to files results.txt and results.csv")

create_results_txt_file()
create_results_csv_file()