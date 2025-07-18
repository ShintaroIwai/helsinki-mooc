# Write your solution here
list = []
action = ""
number = 0
print(f"The list is now {list}")
while action != "x":
    action = input("a(d)d, (r)emove or e(x)it: ")
    if action == "x":
        break
    if action == "d":
        number += 1
        list.append(number)
        print(f"The list is now {list}")
    elif action == "r":
        # remove last item in the list
        list.pop(-1)
        print(f"The list is now {list}")
        number -= 1
    else:
        print("This is not a valid option!")
print("Bye!")
