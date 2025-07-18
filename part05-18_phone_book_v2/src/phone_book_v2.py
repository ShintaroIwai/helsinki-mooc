# Write your solution here
phonebook = []

while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))
    if command == 3:
        print("quitting...")
        break
    elif command == 2:
        # add to dictionary but don't replace
        name = input("name: ")
        number = input("number: ")
        phonebook.append(name)
        phonebook.append(number)
        print("ok!")
    elif command == 1:
        name = input("name: ")
        # search within dictionary but return all numbers
        if name in phonebook:
            for i in range(len(phonebook)):
                if phonebook[i] == name:
                    print(phonebook[i+1])
        else:
            print("no number")
    else:
        print("Not a valid input")