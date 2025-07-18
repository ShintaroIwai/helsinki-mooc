# Write your solution here
def add_student(database: dict, student: str):
    # add students to database
    database[student] = []
    return database

def average_grade(course_list: list):
    # takes a list of tuples (course, grade) - basically "database[student]"
    sum_of_grade = 0
    for course in course_list:
        sum_of_grade += course[1]

    average = sum_of_grade / len(course_list)

    return average

def print_student(database: dict, student: str):
    # print student data
    if student in database:
        individual_course_list = database[student]
        if individual_course_list == []:
            print(f"{student}:")
            print(" no completed courses")
        else:
            print(f"{student}:")
            print(f" {len(individual_course_list)} completed courses:")
            for item in individual_course_list:
                print("  " + item[0], item[1])
            # print average grade as well
            print(f" average grade {average_grade(individual_course_list)}")

    else:
        print(f"{student}: no such person in the database")

def add_course(database: dict, student: str, course_and_grade: tuple):
    # add course and grades (tuple) to student database
    if student in database:
        ind_course_and_grade_list = database[student]
        course, grade = course_and_grade
        # ICL is a list of tuples [(course, grade), (course, grade), ...]
        # ignore course if the grade is lower than the previous time the student took it
        already_exists = False
        for i in range(len(ind_course_and_grade_list)):
            ind_course, ind_grade = ind_course_and_grade_list[i]
            already_exists = course == ind_course
            if already_exists:
                # only when new grade is higher than old grade, overwrite
                if course == ind_course and grade > ind_grade:
                    ind_course_and_grade_list[i] = course_and_grade
                break
        # add the course and grade to list if it doesn't exist, if the grade is 0 then don't add
        if not already_exists and grade > 0:
            ind_course_and_grade_list.append(course_and_grade)
    return database

def count_students(database: dict):
    # count the number of students
    count = len(database)
    return count

def most_courses_completed(database: dict):
    # return the student with most courses completed and the number of courses this person took -> maybe return a tuple?
    highest_person = ""
    highest_number_of_courses = 0
    for student in database:
        student_course_list = database[student]
        courses_completed = len(student_course_list)
        if courses_completed > highest_number_of_courses:
            # replace highest number of courses and person with most courses if current person took more courses
            highest_number_of_courses = courses_completed
            highest_person = student
    
    return (highest_person, highest_number_of_courses)

def best_average_grade(database: dict):
    # return the student with the best average grade
    best_average_grade_person = ""
    best_average_grade = 0
    for student in database:
        student_course_list = database[student]
        ind_average_grade = average_grade(student_course_list)
        if ind_average_grade > best_average_grade:
            best_average_grade_person = student
            best_average_grade = ind_average_grade
    
    return (best_average_grade_person, best_average_grade)

def summary(database: dict):
    student_count = count_students(database)
    print("students", student_count)
    most_courses = most_courses_completed(database)
    max_courses_person = most_courses[0]
    max_courses_grade = most_courses[1]
    print("most courses completed", max_courses_grade, max_courses_person)
    average_grade_tuple = best_average_grade(database)
    best_mean_student = average_grade_tuple[0]
    best_mean_grade = average_grade_tuple[1]
    print("best average grade", best_mean_grade, best_mean_student)

if __name__ == "__main__":

    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)