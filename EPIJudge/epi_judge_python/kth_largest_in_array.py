import random

# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k, A):
    lo, hi = 0, len(A) - 1

    while True:
        keyIdx = random.randint(lo, hi)
        key = A[keyIdx]
        A[keyIdx], A[hi] = A[hi], A[keyIdx]
        front, back = lo, hi - 1
        # front, back = lo, hi

        while front <= back:
            if A[front] > key:
                front += 1
            else:
                A[front], A[back] = A[back], A[front]
                back -= 1

        # for i in range(front, back):
        #     if A[i] > key:
        #         A[i], A[front] = A[front], A[i]
        #         front += 1


        A[front], A[hi] = A[hi], A[front]

        if front == k - 1:
            return key
        elif front > k - 1:
            hi = front - 1
        else:
            lo = front + 1
    return key

from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.tsv',
                                       find_kth_largest))
