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

def add_number(sudoku : list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number

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

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)