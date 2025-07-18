# Converting user input into a list of integers
def user_input():
    user_input_list = []
    keep_going = True
    while keep_going:
        scores = input("Exam points and exercises completed: ")
        x = scores.split()
        for i in x:
            user_input_list.append(int(i))
        keep_going = scores != ""
    return user_input_list

# Split the integer list into a list of exam scores and exercise scores
def exam_points(user_input_list : list):
    exam_points_list = user_input_list[::2]
    return exam_points_list

def exercise_points(user_input_list : list):
    exercise_points_list = user_input_list[1::2]
    return exercise_points_list

# Calculate exam + exercise points (dividing exercise percentage by 10 and round it down)
def overall_points(exam_points_list : list, exercise_points_list : list):
    overall_points_list = []
    for i in range(len(exam_points_list)):
        overall_points = exam_points_list[i] + exercise_points_list[i] // 10
        overall_points_list.append(overall_points)
    return overall_points_list

# Calculate grade
def grade(exam_points_list : list, overall_points_list : list):
    grade = ""
    grade_list = []
    for i in range(len(overall_points_list)):
        if exam_points_list[i] < 10:
            grade = 0
        elif overall_points_list[i] < 15:
            grade = 0
        elif overall_points_list[i] < 18:
            grade = 1
        elif overall_points_list[i] < 21:
            grade = 2
        elif overall_points_list[i] < 24:
            grade = 3
        elif overall_points_list[i] < 27:
            grade = 4
        else:
            grade = 5
        grade_list.append(grade)
    return grade_list

# Calculate statistics
def mean(overall_points_list : list):
    average = sum(overall_points_list) / len(overall_points_list)
    return average

def pass_percentage(grade_list : list):
    percentage = 100 * (1 - (grade_list.count(0) / len(grade_list)))
    return percentage

def grade_distribution(grade_list : list):
    print("Grade distribution:")
    count = 0
    for i in range(5, -1, -1):
        count = grade_list.count(i)
        print(f"  {i}: {'*' * count}")

def main():
    score_list = user_input()
    exam_scores = exam_points(score_list)
    exercise_scores = exercise_points(score_list)
    overall_scores = overall_points(exam_scores, exercise_scores)
    grades = grade(exam_scores, overall_scores)
    points_average = mean(overall_scores)
    percentage = pass_percentage(grades)
    print("Statistics:")
    print(f"Points average: {points_average}")
    print(f"Pass percentage: {percentage:.1f}")
    grade_distribution(grades)

main()