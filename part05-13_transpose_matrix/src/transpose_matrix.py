# Write your solution here
def transpose(matrix: list):
    done_matrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if [i, j] not in done_matrices:
                a = matrix[i][j]
                b = matrix[j][i]
                matrix[i][j] = b
                matrix[j][i] = a
                done_matrices.append([i, j])
                done_matrices.append([j, i])
            # breakpoint()
            # store i and j values in a list and then if in list do the matrix thing?

    #     new_list = []
    # for i in range(len(matrix)):
    #     new_row = []
    #     for j in range(len(matrix[i])):
    #         new_row.append(matrix[j][i])
    #     new_list.append(new_row)

    # return new_list

if __name__ == "__main__":
    my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transpose(my_list)
    print(my_list)