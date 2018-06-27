def has_three_sum(A, t):
    A.sort()

    for i in range(len(A)):
        key = t - A[i]
        l_idx, r_idx = i, len(A) - 1

        while l_idx <= r_idx:
            tempSum = A[l_idx] + A[r_idx]
            if tempSum == key:
                return True
            elif tempSum < key:
                l_idx += 1
            else:
                r_idx -= 1

    return False


from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(generic_test.generic_test_main("three_sum.tsv", has_three_sum))
