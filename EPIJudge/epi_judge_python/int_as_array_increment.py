def plus_one(A):
    for i in range(len(A) - 1, -1, -1):
        if A[i] == 9:
            A[i] = 0
        else:
            A[i] += 1
            break

    if A[0] == 0:
        A.insert(0, 1)

    return A


from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.tsv", plus_one))
