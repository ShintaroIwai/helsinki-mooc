# Write your solution here
class OrderBookApplication:
    def __init__(self):
        self.__orderbook = OrderBook()

    def help(self):
        print("commands:")
        print("0 exit 1 add order 2 list finished tasks 3 list unfinished tasks 4 mark task as finished 5 programmers 6 status of programmer")

    def execute(self):
        self.help()
        while True:
            print("")
            command = int(input("command: "))
            if command == 0:
                break
            elif command == 1:
                self.add()
            elif command == 2:
                self.finished()
            elif command == 3:
                self.unfinished()
            elif command == 4:
                self.id()
            elif command == 5:
                self.programmers()
            elif command == 6:
                self.status_of_tasks()
        
    def add(self):
        description = input("description: ")
        programmer_and_workload = input("programmer and workload estimate: ")
        if " " in programmer_and_workload and len(programmer_and_workload.split(" ")) == 2:
            programmer, workload = programmer_and_workload.split(" ")
            if workload.isdigit():
                self.__orderbook.add_order(description, programmer, workload)
                print("added!")
            else:
                print("erroneous input")
        else:
            print("erroneous input")
    
    def finished(self):
        finished = self.__orderbook.finished_orders()
        if finished == []:
            print("no finished tasks")
        else:
            for task in finished:
                print(task)

    def unfinished(self):
        unfinished = self.__orderbook.unfinished_orders()
        if unfinished == []:
            print("no unfinished tasks")
        else:
            for task in unfinished:
                print(task)
    
    def id(self):
        id = (input("id: "))
        if id.isdigit():
            if int(id) <= len(self.__orderbook):
                self.__orderbook.mark_finished(int(id))
                print("marked as finished")
            else:
                print("erroneous input")
        else:
            print("erroneous input")
    
    def programmers(self):
        names = self.__orderbook.programmers()
        [print(name) for name in names]
    
    def status_of_tasks(self):
        programmer = input("programmer: ")
        if programmer in self.__orderbook.programmers():
            status = self.__orderbook.status_of_programmer(programmer)
            print(f"tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]}")
        else:
            print("erroneous input")

# If you use the classes made in the previous exercise, copy them here
class OrderBook:
    def __init__(self):
        self.__orders = []
    
    def __len__(self):
        return len(self.__orders)

    def add_order(self, description, programmer, workload):
        self.__orders.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.__orders
    
    def programmers(self):
        # only contain each programmer once
        self.names = []
        for order in self.__orders:
            if order.programmer not in self.names:
                self.names.append(order.programmer)
        return self.names
    
    def mark_finished(self, id: int):
        id_found = False
        for order in self.__orders:
            if id == order.id:
                order.mark_finished()
                id_found = True
        if not id_found:
            raise ValueError("There is no order with that ID!")
    
    def finished_orders(self):
        return [order for order in self.__orders if order.is_finished()]
    
    def unfinished_orders(self):
        return [order for order in self.__orders if not order.is_finished()]
    
    def status_of_programmer(self, programmer: str):
        finished = 0
        unfinished = 0
        hours_finished = 0
        hours_unfinished = 0
        found = False
        for order in self.__orders:
            if programmer == order.programmer:
                found = True
                if order.is_finished():
                    finished += 1
                    hours_finished += int(order.workload)
                else:
                    unfinished += 1
                    hours_unfinished += int(order.workload)
        if not found:
            raise ValueError("This programmer hasn't been assigned a task!")
        return (finished, unfinished, hours_finished, hours_unfinished)

class Task:
    instance_count = 0

    def __init__(self, description, programmer, workload):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.state = False
        Task.instance_count += 1
        self.id = Task.instance_count
    
    def mark_finished(self):
        self.state = True
    
    def is_finished(self):
        return self.state

    def __str__(self):
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {'FINISHED' if self.state else 'NOT FINISHED'}"
    

application = OrderBookApplication()
application.execute()