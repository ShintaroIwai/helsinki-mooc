
# WRITE YOUR SOLUTION HERE:
#Note! Do not change the class Person!

class Person:
    def __init__(self, name: str, age: int, height: int, weight: int):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

class BabyCentre:
    def __init__(self):
        self.number_of_weigh_ins = 0

    def weigh(self, person: Person):
        self.number_of_weigh_ins += 1
        # return the weight of the person passed as an argument
        return person.weight
    
    def feed(self, person: Person):
        person.weight += 1

    def weigh_ins(self):
        return self.number_of_weigh_ins

if __name__ == "__main__":
    baby_centre = BabyCentre()

    eric = Person("Eric", 1, 110, 7)
    peter = Person("Peter", 33, 176, 85)

    # print(f"{eric.name} weighs {baby_centre.weigh(eric)} kg")
    # print(f"{peter.name} weighs {baby_centre.weigh(peter)} kg")
    # print() 

    # baby_centre.feed(eric)
    # baby_centre.feed(eric)
    # baby_centre.feed(eric)

    # print(f"{eric.name} weighs {baby_centre.weigh(eric)} kg")
    # print(f"{peter.name} weighs {baby_centre.weigh(peter)} kg")

    print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

    baby_centre.weigh(eric)
    baby_centre.weigh(eric)

    print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

    baby_centre.weigh(eric)
    baby_centre.weigh(eric)
    baby_centre.weigh(eric)
    baby_centre.weigh(eric)

    print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")