# Write your solution here
def open_start_times():
    import csv
    from datetime import datetime

    start_times = {}
    with open("src/start_times.csv") as new_file:
        for line in csv.reader(new_file, delimiter = ";"):
            name = line[0]
            time = line[1]
            start_times[name] = datetime.strptime(time, "%H:%M")
    return start_times
    
def open_submissions():
    import csv

    submissions = []
    with open("src/submissions.csv") as my_file:
        for line in csv.reader(my_file, delimiter = ";"):
            submissions.append(line)
    return submissions

def score_data():
    from datetime import datetime, timedelta
    start_times = open_start_times()
    submissions = open_submissions()
    points_dict = {}
    # want dict to be key = name, value is another dict where the key is task and the value is points
    for name in start_times:
        task_scores = {} # this needs to be inside the loop
        for row in submissions:
            if name == row[0]:
                task = row[1]
                points = int(row[2])
                submit_time = datetime.strptime(row[3], "%H:%M")
                time_allowed = timedelta(hours = 3)
                if submit_time <= start_times[name] + time_allowed:
                    if task in task_scores:
                        high_score = task_scores[task]
                        if points > high_score:
                            task_scores[task] = points
                    else:
                        task_scores[task] = points

            else:
                continue
        points_dict[name] = task_scores
    
    return points_dict

def final_points():
    score_dict = score_data()
    final_dict = {}
    for name in score_dict:
        sum = 0
        scores = score_dict[name]
        for key in scores:
            sum += scores[key]
        final_dict[name] = sum

    return final_dict

# def cheaters():
#     start_times = open_start_times()
#     submissions = open_submissions()
#     cheated = []
#     from datetime import datetime, timedelta
#     for item in start_times:
#         name = item
#         start_time = start_times[item]
#         for row in submissions:
#             submit_time = datetime.strptime(row[3],"%H:%M")
#             if row[0] == name:
#                 allowed = timedelta(hours = 3)
#                 if submit_time > start_time + allowed:
#                     cheated.append(name)
#                     break
#     return cheated

if __name__ == "__main__":
    print(final_points())