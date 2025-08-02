# Write your solution here:
class OrderBook:
    def __init__(self):
        self.__orders = []

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
                    hours_finished += order.workload
                else:
                    unfinished += 1
                    hours_unfinished += order.workload
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
    
if __name__ == "__main__":
    # t1 = Task("program hello world", "Eric", 3)
    # print(t1.id, t1.description, t1.programmer, t1.workload)
    # print(t1)
    # print(t1.is_finished())
    # t1.mark_finished()
    # print(t1)
    # print(t1.is_finished())
    # t2 = Task("program webstore", "Adele", 10)
    # t3 = Task("program mobile app for workload accounting", "Eric", 25)
    # print(t2)
    # print(t3)

    # orders = OrderBook()
    # orders.add_order("program webstore", "Adele", 10)
    # orders.add_order("program mobile app for workload accounting", "Eric", 25)
    # orders.add_order("program app for practising mathematics", "Adele", 100)

    # for order in orders.all_orders():
    #     print(order)

    # print()

    # for programmer in orders.programmers():
    #     print(programmer)

    # orders = OrderBook()
    # orders.add_order("program webstore", "Adele", 10)
    # orders.add_order("program mobile app for workload accounting", "Eric", 25)
    # orders.add_order("program app for practising mathematics", "Adele", 100)

    # orders.mark_finished(1)
    # orders.mark_finished(2)

    # for order in orders.all_orders():
    #     print(order)

    # t = OrderBook()
    # t.add_order("program web store", "Andy", 10)
    # unfinished = t.unfinished_orders()

    # u = OrderBook()
    # u.add_order("program web store", "Andy", 10)
    # u.add_order("program mobile gane", "Eric", 5)
    # u.add_order("code better facebook", "Jonas", 5000)
    # u.mark_finished(1)
    # u.mark_finished(2)
    # u.finished_orders()
    # u.unfinished_orders()

    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)