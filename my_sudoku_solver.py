def check_sudoku(grid):
    return(
        check_rows(grid) and
        check_columns(grid) and
        check_squares(grid)
    )

def check_rows(grid):
    return True

def check_columns(grid):
    return True

def check_squares(grid):
    return True
