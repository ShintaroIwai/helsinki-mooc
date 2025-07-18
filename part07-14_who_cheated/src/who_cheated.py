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

def cheaters():
    start_times = open_start_times()
    submissions = open_submissions()
    cheated = []
    from datetime import datetime, timedelta
    for item in start_times:
        name = item
        start_time = start_times[item]
        for row in submissions:
            submit_time = datetime.strptime(row[3],"%H:%M")
            if row[0] == name:
                allowed = timedelta(hours = 3)
                if submit_time > start_time + allowed:
                    cheated.append(name)
                    break
    return cheated

if __name__ == "__main__":
    print(cheaters())