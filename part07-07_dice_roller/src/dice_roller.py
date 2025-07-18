# Write your solution here
from random import choice

# function for individual rolls
def roll(die: str):
    A = [3, 3, 3, 3, 3, 6]
    B = [2, 2, 2, 5, 5, 5]
    C = [1, 4, 4, 4, 4, 4]
    result = ""
    try:
        if die == "A":
            result = choice(A)
        elif die == "B":
            result = choice(B)
        elif die == "C":
            result = choice(C)
    except ValueError:
        print("Not a valid value, please enter either A, B, or C")

    # could have done
    # dice = {"A" : [3, 3, 3, 3, 3, 6],
    #         "B" : [2, 2, 2, 5, 5, 5],
    #         "C" : [1, 4, 4, 4, 4, 4]}
    # return sample(dice[die], 1)[0]
    
    return int(result)

# throwing dice a specified number of times
def play(die1: str, die2: str, times: int):
    # create three variables to count outcomes and then return them in a tuple
    die1win = 0
    die2win = 0
    tie = 0
    # roll the die specified number of times
    try:
        for i in range(times):
            roll1 = roll(die1)
            roll2 = roll(die2)
            if roll1 > roll2:
                die1win += 1
            elif roll1 < roll2:
                die2win += 1
            else:
                # this is when roll1 == roll2
                tie += 1
    except ValueError:
        print("This is not a valid input!")
    
    return (die1win, die2win, tie)

if __name__ == "__main__":
    # testing the "roll" function
    # for i in range(20):
    #     print(roll("A"), " ", end="")
    # print()
    # for i in range(20):
    #     print(roll("B"), " ", end="")
    # print()
    # for i in range(20):
    #     print(roll("C"), " ", end="")
    # testing the "play" function
    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)