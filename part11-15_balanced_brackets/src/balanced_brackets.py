
def balanced_brackets(my_string: str):
    
    if len(my_string) == 0:
        return True
    
    # if len(my_string) == 2:
    #     if my_string[0] == '(' and my_string[-1] == ')' or my_string[0] == "[" and my_string[-1] == "]":
    #         return True
    
    brackets = "()[]"
    new_string = ""
    for char in my_string:
        if char in brackets:
            new_string += char
            
    if not (new_string[0] == '(' and new_string[-1] == ')') and not (new_string[0] == "[" and new_string[-1] == "]"):
        return False

    # remove first and last character
    return balanced_brackets(new_string[1:-1])

if __name__ == "__main__":
    ok = balanced_brackets("([([])])")
    print(ok)

    ok = balanced_brackets("(python version [3.7]) please use this one!")
    print(ok)

    # this is no good, the closing bracket doesn't match
    ok = balanced_brackets("(()]")
    print(ok)

    # different types of brackets are mismatched
    ok = balanced_brackets("([bad egg)]")
    print(ok)