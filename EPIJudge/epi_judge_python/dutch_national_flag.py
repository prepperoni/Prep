import functools
from sys import exit

from test_framework import generic_test, test_utils
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index, A):
   # close to the book solution
   # key = A[pivot_index]
   # small, equal, large = 0, 0, len(A) - 1

   # while equal <= large:
   #    if A[equal] == key:
   #       equal += 1
   #    elif A[equal] < key: 
   #       A[small], A[equal] = A[equal], A[small]
   #       equal += 1
   #       small += 1
   #    else:
   #       A[equal], A[large] = A[large], A[equal]
   #       large -= 1
    key = A[pivot_index]
    small, match, large = 0, len(A) - 1, len(A) - 1

    while small <= match:
        cur = A[small]
        if cur < key:
            small += 1
        elif cur > key:
            A[small], A[large] = A[large], A[small]
            large -= 1
            if match > large:
                match -= 1
        else:
            A[small], A[match] = A[match], A[small]
            match -= 1

@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
