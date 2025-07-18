# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year
    
    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"
    
    def value(self):
        # have to subtract 1 from month because the month isn't done yet (year starts from 0 so it's ok)
        return (self.year) * 360 + (self.month - 1) * 30 + self.day
    
    def convert_back(self, value: int):
        # converting back from the "value" format defined above
        year = value // 360
        # need to add one to month because for example it can be January even if the first month hasn't finished
        month = (value - year * 360) // 30 + 1
        day = (value - year * 360) % 30
        converted = SimpleDate(day, month, year)
        return converted

    def __lt__(self, another):
        return self.value() < another.value()
    
    def __gt__(self, another):
        return self.value() > another.value()
    
    def __eq__(self, another):
        return self.value() == another.value()
    
    def __ne__(self, another):
        return self.value() != another.value()
    
    def __add__(self, days: int):
        result = self.value() + days
        return self.convert_back(result)
    
    def __sub__(self, another):
        return abs(self.value() - another.value())

if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)
