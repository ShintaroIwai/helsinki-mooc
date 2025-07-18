# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.people = []
    
    def add(self, person: Person):
        self.people.append(person)
    
    def is_empty(self):
        return len(self.people) == 0
    
    def print_contents(self):
        for person in self.people:
            print(f"{person.name} ({person.height} cm)")
    
    def shortest(self):
        if len(self.people) > 0:
            shortest_person = self.people[0]
            minimum_height = self.people[0].height
            for person in self.people:
                if person.height < minimum_height:
                    shortest_person = person
                    minimum_height = person.height
            return shortest_person
        else:
            return None
    
    def remove_shortest(self):
        shortest_person = self.shortest()
        if shortest_person is not None:
            self.people.remove(shortest_person)
            return shortest_person
        else:
            return None

if __name__ == "__main__":
    # room = Room()

    # print("Is the room empty?", room.is_empty())
    # print("Shortest:", room.shortest())

    # room.add(Person("Lea", 183))
    # room.add(Person("Kenya", 172))
    # room.add(Person("Nina", 162))
    # room.add(Person("Ally", 166))

    # print()

    # print("Is the room empty?", room.is_empty())
    # print("Shortest:", room.shortest())

    # print()

    # room.print_contents()

    room = Room()

    room.add(Person("Ann",120))
    room.add(Person("Tim",150))

    # room.add(Person("Lea", 183))
    # room.add(Person("Kenya", 172))
    # room.add(Person("Nina", 162))
    # room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()
