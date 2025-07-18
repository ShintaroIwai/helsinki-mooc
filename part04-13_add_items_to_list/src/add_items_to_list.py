# Write your solution here
number = int(input("How many items: "))
list = []
index = 0
while index < number:
    item = int(input(f"Item {index + 1}: "))
    list.append(item)
    index += 1
print(list)