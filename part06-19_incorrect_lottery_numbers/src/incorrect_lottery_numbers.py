# Write your solution here
def filter_incorrect():
    lottery_list = read_file()
    correct_weeks = week_check(lottery_list)
    correct_numbers = number_check(lottery_list)
    correct_entries = both_check(lottery_list, correct_weeks, correct_numbers)
    create_csv(correct_entries)

def read_file():
    lottery_list = []
    with open ("src/lottery_numbers.csv") as my_file:
        for line in my_file:
            line = line.strip()
            # parts is a list here
            parts = line.split(";")
            header = parts[0]
            lottery_number = parts[1].split(",")
            weekly_tuple = (header, lottery_number)
            lottery_list.append(weekly_tuple)
    return lottery_list

def week_check(lottery_list: list):
    # list of weeks with correct week formatting
    week_correct = []
    for row in lottery_list:
        header = row[0]
        parts = header.split()
        week_number = parts[1]
        try:
            if int(week_number) >= 1:
                week_correct.append(header)
        except ValueError:
            continue
    return week_correct

def number_check(lottery_list: list):
    # list of set of numbers with correct formatting (need to have 7 valid values + can't repeat numbers)
    number_correct = []
    for row in lottery_list:
        # pull out the list of numbers from the tuple 
        number_list = row[1]
        # to use for a later check that the same number doesn't appear twice in the list
        already_appeared = []
        # check for seven numbers in each list
        try:
            if len(number_list) == 7:
                for number in number_list:
                    # Boolean to keep track of whether the list is eligible
                    valid_list = False
                    # check that numbers are correct (not like "**" or "22b")
                    # check that numbers are between 1 and 39
                    if type(int(number)) == int:
                        # check that the same number doesn't appear twice in the list
                        if int(number) in already_appeared:
                            valid_list = False
                        elif int(number) > 0 and int(number) < 40:
                            valid_list = True
                            already_appeared.append(int(number))
                    if valid_list == False:
                        break
                # I think this should be when all 7 are true since hitting a since False should break the loop
                if valid_list == True:
                    number_correct.append(number_list)
        except ValueError:
            continue
    return number_correct

# check which weeks have both the week and number formatting correct
def both_check(lottery_list: list, week_correct: list, number_correct: list):
    valid_week_list = []
    for row in lottery_list:
        week = row[0]
        numbers = row[1]
        if week in week_correct:
            if numbers in number_correct:
                valid_week = (week, numbers)
                valid_week_list.append(valid_week)
    return valid_week_list

def create_csv(valid_week_list: list):
    # takes the valid entries and writes it in a csv file
    with open("correct_numbers.csv", "w") as my_file:
        for row in valid_week_list:
            week = row[0]
            numbers = row[1]
            line = ""
            for i in range(len(numbers)):
                number = numbers[i]
                # if it's the last number in the loop then don't add comma
                if i == len(numbers) - 1:
                    line += f"{number}"
                else:
                    line += f"{number},"
            my_file.write(f"{week};{line}\n")

if __name__ == "__main__":
    # testing read_file function
    # output = read_file()
    # print(output)
    # testing the week_check function
    # print(week_check(output))
    # testing the number_check function
    # print(number_check(output))
    # good_weeks = week_check(output)
    # good_numbers = number_check(output)
    # valid_weeks = both_check(output, good_weeks, good_numbers)
    # create_csv(valid_weeks)
    filter_incorrect()

