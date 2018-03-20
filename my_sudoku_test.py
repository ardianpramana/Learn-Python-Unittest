import unittest
from my_sudoku_solver import *

class MySudokuTest(unittest.TestCase):
    def test(self):
        # rows add to 9, column add to 9, and the
        # nine 3 x 3 squares all common digits 1 - 9
        valid_grid = [[4, 3, 5, 2, 6, 9, 7, 8, 1],
                      [6, 8, 2, 5, 7, 1, 4, 9, 3],
                      [1, 9, 7, 8, 3, 4, 5, 6, 2],
                      [8, 2, 6, 1, 9, 5, 3, 4, 7],
                      [3, 7, 4, 6, 8, 2, 9, 1, 5],
                      [9, 5, 1, 7, 4, 3, 6, 2, 8],
                      [5, 1, 9, 3, 2, 6, 8, 7, 4],
                      [2, 4, 8, 9, 5, 7, 1, 3, 6],
                      [7, 6, 3, 4, 1, 8, 2, 5, 9]]

        invalid_grid = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                        [1, 2, 3, 4, 5, 6, 7, 8, 9],
                        [1, 2, 3, 4, 5, 6, 7, 8, 9],
                        [1, 2, 3, 4, 5, 6, 7, 8, 9],
                        [1, 2, 3, 4, 5, 6, 7, 8, 9],
                        [1, 2, 3, 4, 5, 6, 7, 8, 9],
                        [1, 2, 3, 4, 5, 6, 7, 8, 9],
                        [1, 2, 3, 4, 5, 6, 7, 8, 9],
                        [1, 2, 3, 4, 5, 6, 7, 8, 9]]

        assert(check_sudoku(valid_grid))
        assert(not check_sudoku(invalid_grid))

        print("Test done")

if __name__ == '__main__':
    unittest.main()