# Write your solution here
from datetime import datetime, timedelta

# test
# file_name = "late_june.txt"
# input_date = "24.6.2020"
# start_date = datetime.strptime(input_date, "%d.%m.%Y")
# number_of_days = 5

file_name = input("Filename: ")
input_date = input("Starting date: ")
start_date = datetime.strptime(input_date, "%d.%m.%Y")
number_of_days = int(input("How many days: "))
print("Please type in screen time in minutes on each day (TV computer mobile):")

date = start_date
with open(file_name, "w") as my_file:
    screen_times = []
    last_day = start_date + timedelta(days = number_of_days - 1)
    end_date = last_day.strftime("%d.%m.%Y")
    total_screen_time = 0
    for i in range(number_of_days):
        screen_time_input = input(f"Screen time {date.strftime('%d.%m.%Y')}: ")
        screen_time = ""
        for char in screen_time_input:
            if char == " ":
                screen_time += "/"
            else:
                screen_time += char
        TV_comp_mobile = screen_time_input.split()
        for item in TV_comp_mobile:
            minutes = int(item)
            total_screen_time += minutes
        day_and_screen_time = (date, screen_time)
        screen_times.append(day_and_screen_time)
        date += timedelta(days = 1)
    average_screen_time = total_screen_time / number_of_days
    my_file.write(f"Time period: {start_date.strftime('%d.%m.%Y')}-{end_date}" + "\n")
    my_file.write(f"Total minutes: {total_screen_time}" + "\n")
    my_file.write(f"Average minutes: {average_screen_time}" + "\n")
    for row in screen_times:
        day_output = row[0].strftime("%d.%m.%Y")
        my_file.write(f"{day_output}: {row[1]}" + "\n")

print(f"Data stored in file {file_name}")
