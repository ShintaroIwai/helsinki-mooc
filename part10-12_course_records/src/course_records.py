# tee ratkaisusi tänne
class CourseDict:
    def __init__(self):
        self._courses = {}

    def add_course(self, name: str, grade: int, credits: int):
        self.add_name(name)
        self.add_grade(name, grade)
        self.add_credits(name, credits)

    def add_name(self, name: str):
        # if the name is the same course, you don't want a new dictionary entry
        if name not in self._courses:
            self._courses[name] = Course(name)
    
    def add_grade(self, name: str, grade: int):
        # the overwrite rules for grades are handled in the Course object
        self._courses[name].add_grade(grade)
    
    def add_credits(self, name: str, credits: int):
        self._courses[name].add_credits(credits)
    
    # def add_course(self, name: str, grade: int, credits: int):
    #     if name not in self.__course_list:
    #         self.__course_list[name] = Course(name)
    #     else:
    #         if self.__course_list[name].grade() < grade:
    #             self.__course_list[name].add_grade(grade)

    def get_grade(self, name: str):
        grade = self._courses[name].grade()
        return grade
    
    def get_credits(self, name: str):
        credits = self._courses[name].credits()
        return credits
    
    def __iter__(self):
        self.n = 0

    def __next__(self):
        if self.n < len(self._courses):
            course = self._courses[self.n]
            self.n += 1
            return course
        else:
            raise StopIteration
    
    def completed_courses(self):
        return len(self._courses)
    
    def completed_credits(self):
        completed = 0
        for course in self._courses:
            credits = self._courses[course].credits()
            completed += credits
        return completed
    
    def mean_grade(self):
        total_grade = 0
        for course in self._courses:
            grade = self._courses[course].grade()
            total_grade += grade
        courses_completed = self.completed_courses()
        mean = total_grade / courses_completed
        return mean
    
    def grade_list(self):
        list = []
        for course in self._courses:
            grade = self._courses[course].grade()
            list.append(grade)
        return list

class Course:
    def __init__(self, name: str):
        # should I use "None" as a starter? Could modify the code later
        self.__name = name
        self.__grade = 0
        self.__credits = 0
    
    def name(self):
        return self.__name
    
    def grade(self):
        return self.__grade
    
    def credits(self):
        return self.__credits

    def add_grade(self, grade: int):
        if grade == 0:
            self.__grade = grade
        # maybe think about if "grade" doesn't exist yet?
        if self.__grade < grade:
            self.__grade = grade
    
    def add_credits(self, credits: int):
        self.__credits = credits

class CourseListApplication:
    def __init__(self):
        self.__course_dict = CourseDict()
    
    def help(self):
        print("1 add course 2 get course 3 statistics 0 exit")
    
    def add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__course_dict.add_course(name, grade, credits)
    
    def get_course(self):
        # have to account for when there is no course entry for the input
        name = input("course: ")
        if name in self.__course_dict._courses:
            grade = self.__course_dict.get_grade(name)
            credits = self.__course_dict.get_credits(name)
            print(f"{name} ({credits} cr) grade {grade}")
        else:
            print("no entry for this course")
    
    def statistics(self):
        completed_courses = self.__course_dict.completed_courses()
        completed_credits = self.__course_dict.completed_credits()
        mean_grade = self.__course_dict.mean_grade()
        print(f"{completed_courses} completed courses, a total of {completed_credits} credits")
        print(f"mean {mean_grade:.1f}")

    def grade_distribution(self):
        grade_list = self.__course_dict.grade_list()
        print("grade distribution")
        for i in range(5, 0, -1):
            count = grade_list.count(i)
            xs = "x" * count
            print(f"{i}: {xs}")
    
    def execute(self):
        self.help()
        while True:
            print("")
            command = int(input("command: "))
            if command == 0:
                break
            elif command == 1:
                self.add_course()
            elif command == 2:
                self.get_course()
            elif command == 3:
                self.statistics()
                self.grade_distribution()
        
application = CourseListApplication()
application.execute()
# if __name__ == "__main__":
#     list = CourseList()
#     # itp = Course("ItP")
#     list.add_course("ItP", 2, 5)
#     list.add_course("ItP", 1, 5)
#     # itp.add_grade(1)
#     # itp.add_credits(5)
#     # print(itp.name())
#     # print(itp.grade())
#     # print(itp.credits())
#     print(list.get_credits("ItP"))
#     print(list.get_grade("ItP"))
    
