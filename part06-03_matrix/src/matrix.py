# write your solution here
def read_file(file_to_read):
    # a function to read a CSV file and then return a list of numbers while putting each line in the CSV in a list
    with open(file_to_read) as new_file:
        numbers_list = []
        for line in new_file:
            each_line = []
            line = line.replace("\n", "")
            parts = (line.split(","))
            for number in parts:
                number = int(number)
                each_line.append(number)
            numbers_list.append(each_line)
    return numbers_list

def matrix_sum():
    # return the sum of all numbers in the matrix (list of lists)
    matrix = read_file("src/matrix.txt")
    sum_of_numbers = 0
    for inner_list in matrix:
        for number in inner_list:
            sum_of_numbers += number
    return sum_of_numbers

def matrix_max():
    # return the maximum value of all numbers in the matrix (list of lists)
    matrix = read_file("src/matrix.txt")
    max_value = 0
    for line in matrix:
        for number in line:
            if number > max_value:
                max_value = number
    return max_value

def row_sums():
    # return the sum of each row as a list
    matrix = read_file("src/matrix.txt")
    sum_list = []
    for line in matrix:
        sum_of_line = 0
        for number in line:
            sum_of_line += number
        sum_list.append(sum_of_line)
    return sum_list

if __name__ == "__main__":
    # print(read_file("src/matrix.txt"))
    sum = matrix_sum()
    print(sum)
    max = matrix_max()
    print(max)
    sum_of_rows = row_sums()
    print(sum_of_rows)