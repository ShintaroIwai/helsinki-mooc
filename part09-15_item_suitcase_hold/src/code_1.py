# Write your solution here:
class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight
    
    def name(self):
        return self.__name
    
    def weight(self):
        # return weight of item
        return self.__weight
    
    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"

class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__items = []

    def add_item(self, item: Item):
        # if the difference between the max weight and the current weight is greater than or equal to the item weight, we can add it to suitcase
        if self.__max_weight - self.weight() >= item.weight():
            self.__items.append(item)
        # else:
        #     raise ValueError("The maximum weight would be exceeded if this item is added!")
    
    def print_items(self):
        for item in self.__items:
            print(item)
    
    def weight(self):
        # return weight of suitcase
        total = 0
        for item in self.__items:
            total += item.weight()
        return total
    
    def heaviest_item(self):
        heaviest = 0
        heaviest_thing = None
        for item in self.__items:
            if item.weight() > heaviest:
                heaviest = item.weight()
                heaviest_thing = item
        return heaviest_thing
    
    def __str__(self):
        count = len(self.__items)
        if count == 1:
            return f"{count} item ({self.weight()} kg)"
        else:
            return f"{count} items ({self.weight()} kg)"

class CargoHold:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__suitcases = []
    
    def add_suitcase(self, suitcase: Suitcase):
        if self.__max_weight - suitcase.weight() >= 0:
            self.__suitcases.append(suitcase)
    
    def weight(self):
        total = 0
        for suitcase in self.__suitcases:
            total += suitcase.weight()
        return total
    
    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()

    def __str__(self):
        number_of_items = len(self.__suitcases)
        remainder = self.__max_weight - self.weight()
        if number_of_items != 1:
            return f"{number_of_items} suitcases, space for {remainder} kg"
        else:
            return f"{number_of_items} suitcase, space for {remainder} kg"

if __name__ == "__main__":
    # Testing part 7
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()

