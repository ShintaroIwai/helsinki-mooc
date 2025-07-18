
# Write your solution here:
class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_number(number)

    def add_address(self, name: str, address: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_address(address)

    def get_number(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name].numbers()
    
    def get_address(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name].address()

    def all_entries(self):
        return self.__persons

class Person:
    def __init__(self, name: str):
        self.__name = name
        self.__numbers = []
        self.__address = ""
    
    def name(self):
        return self.__name
    
    def numbers(self):
        return self.__numbers
    
    def address(self):
        if self.__address != "":
            return self.__address
        else:
            return None
    
    def add_number(self, number: str):
        self.__numbers.append(number)

    def add_address(self, address: str):
        self.__address = address

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)
    
    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)

    def search(self):
        name = input("name: ")
        numbers = self.search_number(name)
        address = self.search_address(name)

        if numbers == None:
            print("number unknown")
        else:
            for number in numbers:
                print(number)
        print(address)

        #     def search(self):
        # name = input("name: ")
        # numbers = self.__phonebook.get_number(name)
        # address = self.__phonebook.get_address(name)
        # if numbers == None:
        #     print("number unknown") 
        #     return 
        # for number in numbers:
        #     print(number)

    def search_number(self, name: str):
        numbers = self.__phonebook.get_number(name)
        if numbers == []:
            return None
        return numbers
    
    def search_address(self, name: str):
        address = self.__phonebook.get_address(name)
        if address == None:
            return "address unknown"
        return address

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()


# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()

# if __name__ == "__main__":
#     person = Person("Eric")
#     print(person.name())
#     print(person.numbers())
#     print(person.address())
#     person.add_number("040-123456")
#     person.add_address("Mannerheimintie 10 Helsinki")
#     print(person.numbers())
#     print(person.address())

    # phonebook = PhoneBook()
    # phonebook.add_number("Eric", "02-123456")
    # phonebook.add_address("Emily", "Viherlaaksontie 7, Espoo")
    # print(phonebook.get_number("Eric"))
    # print(phonebook.get_address("Emily"))
