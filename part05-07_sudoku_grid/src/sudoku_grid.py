# Check for duplicates in rows
def row_correct(sudoku: list, row_no: int):
    # check if there are duplicates of 1-9 in the row number selected
    used_number_list = []
    for i in range(len(sudoku[row_no])):
        if sudoku[row_no][i] in used_number_list:
            return False
        if sudoku[row_no][i] != 0:
            used_number_list.append(sudoku[row_no][i])
    
    return True

# Check for duplicates in columns
def column_correct(sudoku: list, column_no: int):
    used_number_list = []
    for i in range(len(sudoku)):
        number = sudoku[i][column_no]
        if number > 0 and number in used_number_list:
            return False
        used_number_list.append(number)
    
    return True

# Check for a 3x3 block for duplicates
def block_correct(sudoku: list, row_no: int, column_no: int):
    used_number_list = []
    for row in sudoku[row_no : row_no + 3]:
        for number in row[column_no : column_no + 3]:
            if number > 0 and number in used_number_list:
                return False
            used_number_list.append(number)

    return True

def sudoku_grid_correct(sudoku: list):
    index_check = [0, 3, 6]
    for i in range(len(sudoku)):
        row_check = row_correct(sudoku, i)
        # if even one of the row check returns false, then sudoku_grid_correct can't return true
        if row_check == False:
            return False
    for j in range(len(sudoku)):
        column_check = column_correct(sudoku, j)
        # if even one of the column check returns false, then sudoku_grid_correct can't return true
        if column_check == False:
            return False
    for k in index_check:
        for l in index_check:
            block_correct(sudoku, k, l)
            if block_correct(sudoku, k, l) == False:
                return False
    
    return True


if __name__ == "__main__":
    sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))

    sudoku3 = [
    [ 2, 6, 7, 8, 3, 9, 5, 0, 4 ],
    [ 9, 0, 3, 5, 1, 0, 6, 0, 0 ],
    [ 0, 5, 6, 0, 0, 0, 8, 3, 9 ],
    [ 5, 1, 9, 0, 4, 6, 3, 2, 8 ],
    [ 8, 0, 2, 1, 0, 5, 7, 0, 6 ],
    [ 6, 7, 4, 3, 2, 0, 0, 0, 5 ],
    [ 0, 0, 0, 4, 5, 7, 2, 6, 3 ],
    [ 3, 2, 0, 0, 8, 0, 0, 5, 7 ],
    [ 7, 4, 5, 0, 0, 3, 9, 0, 1 ],
    ]
    print(sudoku_grid_correct(sudoku3))