# Write your solution here
while True:
    with open("diary.txt") as new_file:
        contents = new_file.read()
    print("1 - add an entry, 2 - read entries, 0 - quit")
    choice = int(input("Function: "))
    # quit
    if choice == 0:
        break
    # add entry
    if choice == 1:
        with open("diary.txt", "a") as writing_file:
            diary_entry = input("Diary entry: ")
            writing_file.write(f"{diary_entry}\n")
        print("Diary saved")
    # read entry
    if choice == 2:
        with open("diary.txt") as reading_file:
            print("Entries:")
            for line in reading_file:
                line = line.strip()
                print(line)

print("Bye now!")
