# Write your solution here:
class LunchCard:
    def __init__(self, balance: int):
        self.balance = balance
    
    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"
    
    def eat_lunch(self):
        if self.balance >= 2.60:
            self.balance -= 2.60
    
    def eat_special(self):
        if self.balance >= 4.60:
            self.balance -= 4.60

    def deposit_money(self, deposit: int):
        if deposit < 0:
            raise ValueError("You cannot deposit an amount of money less than zero")
        self.balance += deposit


peters_card = LunchCard(20)
graces_card = LunchCard(30)
peters_card.eat_special()
graces_card.eat_lunch()
print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")
peters_card.deposit_money(20)
graces_card.eat_special()
print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")
peters_card.eat_lunch()
peters_card.eat_lunch()
graces_card.deposit_money(50)
print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")

# card = LunchCard(50)
# print(card)

# card.eat_lunch()
# print(card)

# card.eat_special()
# card.eat_lunch()
# print(card)

# card = LunchCard(10)
# print(card)
# card.deposit_money(15)
# print(card)
# card.deposit_money(10)
# print(card)
# card.deposit_money(200)
# print(card)