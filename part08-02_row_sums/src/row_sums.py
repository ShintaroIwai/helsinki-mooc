# Write your solution here
def row_sums(my_matrix: list):
    for row in my_matrix:
        # row.append(sum(row))
        new_number = 0
        for number in row:
            new_number += number
        row.append(new_number)

if __name__ == "__main__":
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)