# Write your solution here!
class NumberStats:
    def __init__(self):
        self.numbers = 0
        self.total = 0

    def add_number(self, number:int):
        self.numbers += 1
        self.total += number

    def count_numbers(self):
        return self.numbers
    
    def get_sum(self):
        return self.total

    def average(self):
        count = self.count_numbers()
        if count > 0:
            mean = self.total / count
        else:
            mean = 0
        return mean
    
# Main program
stats = NumberStats()
even_stats = NumberStats()
odd_stats = NumberStats()
while True:
    number = int(input("Please type in integer numbers: "))
    if number == -1:
        break
    else:
        stats.add_number(number)
        if number % 2 == 0:
            even_stats.add_number(number)
        else:
            odd_stats.add_number(number)

print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:", even_stats.get_sum())
print("Sum of odd numbers:", odd_stats.get_sum())

# stats = NumberStats()
# stats.add_number(3)
# stats.add_number(5)
# stats.add_number(1)
# stats.add_number(2)
# print("Numbers added:", stats.count_numbers())
# print("Sum of numbers:", stats.get_sum())
# print("Mean of numbers:", stats.average())