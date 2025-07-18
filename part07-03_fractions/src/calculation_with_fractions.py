# Write your solution here
def fractionate(amount: int):
    # creating an empty list to put the fractions in
    fraction_list = []

    from fractions import Fraction

    for i in range(amount):
        number = Fraction(1, amount)
        fraction_list.append(number)
    
    return fraction_list

if __name__ == "__main__":
    for p in fractionate(3):
        print(p)
    
    print()

    print(fractionate(5))