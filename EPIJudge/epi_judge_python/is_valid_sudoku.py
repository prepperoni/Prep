# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(board):
    def check_rc(x, is_row):
        s = set()

        for i in range(9):
            val = board[x][i] if is_row else board[i][x]
            if val in s:
                return False
            if val > 0:
                s.add(val)

        return True

    def check_sq(x, y):
        s = set()

        for i in range(3):
            for j in range(3):
                val = board[x+i][y+j]
                if val in s:
                    return False
                if val > 0:
                    s.add(val)

        return True              

    for i in range(9):
        if not check_rc(i, True) or not check_rc(i, False):
            return False


    for i in range(3):
        for j in range(3):
            if not check_sq(i*3, j*3):
                return False

    return True


from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_sudoku.tsv", is_valid_sudoku))
