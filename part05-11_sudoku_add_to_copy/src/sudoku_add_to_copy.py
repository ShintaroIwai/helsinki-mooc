# Write your solution here
def print_sudoku(sudoku : list):
    row_no = 0
    for row in sudoku:
        if row_no == 3 or row_no == 6:
            print()
        for i in range(len(row)):
            if i == 2 or i == 5:
                if row[i] == 0:
                    print("_  ", end = "")
                else:
                    print(f"{row[i]}  ", end = "")
            elif i == 8:
                if row[i] == 0:
                    print("_ ")
                else:
                    print(row[i], "")
            else:
                if row[i] == 0:
                    print("_ ", end = "")
                else:
                    print(row[i], "", end = "")
        row_no += 1

def copy_and_add(sudoku : list, row_no: int, column_no: int, number: int):
    new_sudoku = []
    for i in range(len(sudoku)):
        new_row = []
        for j in range(len(sudoku[i])):
            if i == row_no and j == column_no:
                new_row.append(number)
            else:
                new_row.append(sudoku[i][j])
        new_sudoku.append(new_row)

    return new_sudoku

# This is the model solution (didn't have to do nested loop):
# def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int):
#     new_list = []
#     for r in sudoku:
#         new_list.append(r[:])
 
#     new_list[row_no][column_no] = number
#     return new_list
    
if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)