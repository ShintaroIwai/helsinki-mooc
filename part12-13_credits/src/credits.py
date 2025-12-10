from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

def credit_sum_helper(credits_sum, course):
    return credits_sum + course.credits
    
# Write your solution
def sum_of_all_credits(attempts_list: list):
    return reduce(credit_sum_helper, attempts_list, 0)

def sum_of_passed_credits(attempts_list: list):
    passed_courses = list(filter(lambda x: x.grade >= 1, attempts_list))
    return sum_of_all_credits(passed_courses)
    # def passed_credit_sum_helper(credits_sum, course):
    #     if course.grade >= 1:
    #         return credits_sum + course.credits
    #     else:
    #         return credits_sum
    
    # return reduce(passed_credit_sum_helper, attempts_list, 0)

def average(attempts_list: list):
    def grade_sum_helper(grade_sum: int, course: CourseAttempt):
        return grade_sum + course.grade

    passed_courses = list(filter(lambda n: n.grade >= 1, attempts_list)) 
    sum_of_grades = reduce(grade_sum_helper, attempts_list, 0)
    return (sum_of_grades / len(passed_courses))

if __name__ == "__main__":
    # part 1
    # s1 = CourseAttempt("Introduction to Programming", 5, 5)
    # s2 = CourseAttempt("Advanced Course in Programming", 4, 5)
    # s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    # credit_sum = sum_of_all_credits([s1, s2, s3])
    # print(credit_sum)

    # part 2
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    credit_sum = sum_of_passed_credits([s1, s2, s3])
    print(credit_sum)

    # part 3
    ag = average([s1, s2, s3])
    print(ag)