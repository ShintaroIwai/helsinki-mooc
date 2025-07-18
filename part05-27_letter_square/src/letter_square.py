# Write your solution here
# list of all letters in the alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# do the lower right corner
def lower_right_corner():
    n = int(input("Layers: "))
    char_list = []
    for i in range(n):
        # alphabet[i] * i + one of every letter after it in the alphabet
        row = alphabet[i] * (i + 1)
        for j in range(i + 1, n):
            row += alphabet[j]
        char_list.append(row)

    return char_list
    
def lower_half(char_list: list):
    # remove the first character of each row, then reverse it and attach to the original row
    right_half_of_row_list = []
    full_row_list = []
    for row in char_list:
        right_half_of_row = row[1:]
        right_half_of_row_list.append(right_half_of_row)
    for i in range(len(char_list)):
        left_half_of_row = right_half_of_row_list[i][::-1]
        full_row = left_half_of_row + char_list[i]
        full_row_list.append(full_row)

    return full_row_list

def full_matrix(row_list: list):
    # takes a list of rows (from lower_half) and makes a list of the full matrix by creating the top half
    full_matrix_list = []
    # append the indiviual strings from row_list but in reverse order
    for row in row_list[::-1]:
        full_matrix_list.append(row)
    # remove the first row of row_list (because you only need it once) and then add the rest of row_list in order
    for row in row_list[1::]:
        full_matrix_list.append(row)

    return full_matrix_list

def print_list(full_matrix_list):
    for row in full_matrix_list:
        print(row)

def main():
    step1 = lower_right_corner()
    step2 = lower_half(step1)
    step3 = full_matrix(step2)
    print_list(step3)

main()
