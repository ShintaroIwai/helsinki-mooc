# Write your solution here
number = int(input("Please type in a positive integer: "))
start_number = -number
for num in range(start_number, number+1):
    if num != 0:
        print(num)