def n_queens(n):
    def recurse(queen_cols, row):
        if row == n:
            res.append(queen_cols[:])
            return

        for c in range(n):
            safe = True
            for queen_row, queen_col in enumerate(queen_cols):
                dist = row - queen_row
                if c == queen_col or c == queen_col - dist or c == queen_col + dist:
                    safe = False
            if safe:
                queen_cols.append(c)
                recurse(queen_cols, row + 1)
                queen_cols.pop()

    res = []
    recurse([], 0)
    return res

def comp(a, b):
    return sorted(a) == sorted(b)


from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(generic_test.generic_test_main('n_queens.tsv', n_queens, comp))
