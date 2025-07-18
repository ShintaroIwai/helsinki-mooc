# Write your solution here
def run(program: list):
    initial = initialize_variables()
    current_variables = initial
    print_list = []
    line_number = 0
    while line_number < len(program):
        line = program[line_number]
        if line.startswith("MOV"):
            mov(line, current_variables)
        elif line.startswith("PRINT"):
            print_value(line, current_variables, print_list)
        elif line.startswith("ADD"):
            add(line, current_variables)
        elif line.startswith("SUB"):
            subtract(line, current_variables)
        elif line.startswith("MUL"):
            multiply(line, current_variables)
        elif line.startswith("JUMP"):
            line_number = jump(line, program)
            # here I want continue b/c it jumps to the next loop without adding 1 to the line number variable
            continue
        elif line.startswith("IF"):
            if_list = line.split()
            command = if_list[4] + " " + if_list[5]
            condition = condition_check(line, current_variables)
            if condition:
                if command.startswith("MOV"):
                    mov(command, current_variables)
                elif command.startswith("PRINT"):
                    print_value(command, current_variables, print_list)
                elif command.startswith("ADD"):
                    add(command, current_variables)
                elif command.startswith("SUB"):
                    subtract(command, current_variables)
                elif command.startswith("MUL"):
                    multiply(command, current_variables)
                elif command.startswith("JUMP"):
                    line_number = jump(command, program)
                    continue
        elif line == "END":
            break
        line_number += 1
    return print_list

    # for i in range(len(program)):
    #     line = program[i]
    #     if line.startswith("MOV"):
    #         mov(line, current_variables)
    #     elif line.startswith("PRINT"):
    #         print_value(line, current_variables, print_list)
    #     elif line.startswith("ADD"):
    #         add(line, current_variables)
    #     elif line.startswith("SUB"):
    #         subtract(line, current_variables)
    #     elif line.startswith("MUL"):
    #         multiply(line, current_variables)
    #     elif line.startswith("JUMP"):
    #         i = jump(line, program)
    #     elif line.startswith("IF"):
    #         if_list = line.split()
    #         command = if_list[4] + " " + if_list[5]
    #         condition = condition_check(line, current_variables)
    #         if condition:
    #             if command.startswith("MOV"):
    #                 mov(command, current_variables)
    #             elif command.startswith("PRINT"):
    #                 print_value(command, current_variables, print_list)
    #             elif command.startswith("ADD"):
    #                 add(command, current_variables)
    #             elif command.startswith("SUB"):
    #                 subtract(command, current_variables)
    #             elif command.startswith("MUL"):
    #                 multiply(command, current_variables)
    #             elif command.startswith("JUMP"):
    #                 breakpoint()
    #                 i = jump(command, program)
    #                 continue
    #         else:
    #             continue
    #     elif line == "END":
    #         break
    #     else:
    #         continue
    # return current_variables

def initialize_variables():
    from string import ascii_uppercase
    # assign 0 to every uppercase letter in the alphabet
    variables = {}
    for char in ascii_uppercase:
        variables[char] = 0
    return variables

def mov(line: str, current_variables: dict):
    from string import ascii_uppercase
    command = line.split()
    variable = command[1]
    value = command[2]
    if value in ascii_uppercase:
        new_value = current_variables[value]
    else:
        new_value = int(command[2])
    current_variables[variable] = new_value
    return current_variables

def print_value(line: str, current_variables: dict, print_list: list):
    from string import ascii_uppercase
    command = line.split()
    variable = command[1]
    value = 0
    if variable in ascii_uppercase:
        value = current_variables[variable]
    else:
        value = int(variable)
    print_list.append(value)
    return print_list

def add(line: str, current_variables: dict):
    from string import ascii_uppercase
    command = line.split()
    variable = command[1]
    number = command[2]
    # if the number to add is a variable then need to get it from dict, if not just convert it to int
    if number in ascii_uppercase:
        number_to_add = current_variables[number]
    else:
        number_to_add = int(number)
    current_value = current_variables[variable]
    new_value = current_value + number_to_add
    current_variables[variable] = new_value
    return current_variables

def subtract(line: str, current_variables: dict):
    from string import ascii_uppercase
    command = line.split()
    variable = command[1]
    number = command[2]
    # if the number to add is a variable then need to get it from dict, if not just convert it to int
    if number in ascii_uppercase:
        number_to_subtract = current_variables[number]
    else:
        number_to_subtract = int(number)
    current_value = current_variables[variable]
    new_value = current_value - number_to_subtract
    current_variables[variable] = new_value
    return current_variables

def multiply(line: str, current_variables: dict):
    from string import ascii_uppercase
    command = line.split()
    variable = command[1]
    number = command[2]
    # if the number to add is a variable then need to get it from dict, if not just convert it to int
    if number in ascii_uppercase:
        number_to_multiply = current_variables[number]
    else:
        number_to_multiply = int(number)
    current_value = current_variables[variable]
    new_value = current_value * number_to_multiply
    current_variables[variable] = new_value
    return current_variables

def jump(line: str, program: list):
    destination = line[5:] + ":" # use the fact that "JUMP " is 5 characters long, use colon so it actually goes where we want it to go
    line_number = 0
    for i in range(len(program)):
        command = program[i]
        if destination in command:
            line_number = i
            break
    return line_number

def condition_check(line: str, current_variables: dict):
    from string import ascii_uppercase
    if_list = line.split()
    letter = if_list[1]
    comparison = if_list[3]
    # creating a comparison variable that can be used either for comparing with variable or number
    if if_list[3] in ascii_uppercase:
        comparison_value = current_variables[comparison]
    else:
        comparison_value = int(comparison)
    variable_value = current_variables[letter]
    statement = f"{variable_value}{if_list[2]}{comparison_value}"
    condition = eval(statement)
    if condition:
        return True
    else:
        return False

if __name__ == "__main__":
    # program1 = []
    # program1.append("MOV A 1")
    # program1.append("MOV B 2")
    # program1.append("PRINT A")
    # program1.append("PRINT B")
    # program1.append("ADD A B")
    # program1.append("PRINT A")
    # program1.append("END")
    # result = run(program1)

    # program2 = []
    # program2.append("MOV A 1")
    # program2.append("MOV B 10")
    # program2.append("begin:")
    # program2.append("IF A >= B JUMP quit")
    # program2.append("PRINT A")
    # program2.append("PRINT B")
    # program2.append("ADD A 1")
    # program2.append("SUB B 1")
    # program2.append("JUMP begin")
    # program2.append("quit:")
    # program2.append("END")
    # result = run(program2)
    # print(result)

    # test for condition_check
    # test_dict = {"A": 4, "B": 3}
    # test = condition_check("IF A > B JUMP quit", test_dict)
    # print(test)

    program5 = ['MOV N 100', 'PRINT 2', 'MOV A 3', 'start:', 'MOV B 2', 'MOV Z 0', 'test:', 'MOV C B', 'new:', 
            'IF C == A JUMP virhe', 'IF C > A JUMP pass_by', 'ADD C B', 'JUMP new', 'virhe:', 'MOV Z 1', 'JUMP pass_by2',
            'pass_by:', 'ADD B 1', 'IF B < A JUMP test', 'pass_by2:', 'IF Z == 1 JUMP pass_by3', 'PRINT A', 'pass_by3:', 'ADD A 1',
            'IF A <= N JUMP start']
    result5 = run(program5)
    print(result5)