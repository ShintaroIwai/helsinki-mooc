# Write your solution here
def retrieve_all():
    import urllib.request, json
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    raw_data = my_request.read()
    data = json.loads(raw_data)
    active_course_list = []
    for row in data:
        full_name = row["fullName"]
        name = row["name"]
        year = row["year"]
        exercises_list = row["exercises"]
        sum = 0
        for number in exercises_list:
            sum += number
        course_data = (full_name, name, year, sum)
        if row["enabled"]:
            active_course_list.append(course_data)
    return active_course_list

def retrieve_course(course_name: str):
    import urllib.request, json
    from math import floor

    my_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    raw_data = my_request.read()
    data = json.loads(raw_data)
    
    info = {}
    # data is stored as a dictionary, keys in the first layer is indicating number of JSON object literals retrieved
    weeks = len(data)
    max_students = 0
    # hours = the sum of all hour_total values in different weeks
    hours = 0
    # exercises = the sum of all exercise_total values in the different weeks
    exercises = 0
    for row in data:
        # week_info is the dictionary within the outer dictionary (this has all the students/hour/exercise info)
        week_info = data[row]
        students = week_info["students"]
        if students > max_students:
            max_students = students
        hour_total = week_info["hour_total"]
        hours += hour_total
        exercise_total = week_info["exercise_total"]
        exercises += exercise_total
    
    # using floor(x) from the math module to round down to the nearest integer
    hours_average = floor(hours / max_students)
    exercises_average = floor(exercises / max_students)

    info["weeks"] = weeks
    info["students"] = max_students
    info["hours"] = hours
    info["hours_average"] = hours_average
    info["exercises"] = exercises
    info["exercises_average"] = exercises_average

    return info

if __name__ == "__main__":
    print(retrieve_all())
    print(retrieve_course("docker2019"))