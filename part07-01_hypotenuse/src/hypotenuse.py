# Write your solution here
def hypotenuse(leg1: float, leg2: float):
    from math import sqrt

    hyp_squared = leg1 ** 2 + leg2 ** 2
    hyp = sqrt(hyp_squared)  
    return hyp

if __name__ == "__main__":
    print(hypotenuse(3,4))