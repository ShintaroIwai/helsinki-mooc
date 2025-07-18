# Write your solution here
phonebook = {}

while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))
    if command == 3:
        print("quitting...")
        break
    elif command == 1:
        name = input("name: ")
        # search within dictionary
        if name in phonebook:
            print(phonebook[name])
        else:
            print("no number")
    elif command == 2:
        # add to dictionary
        name = input("name: ")
        number = input("number: ")
        phonebook[name] = number
        print("ok!")
    else:
        print("Not a valid input")