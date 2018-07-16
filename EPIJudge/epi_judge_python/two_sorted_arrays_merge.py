from test_framework import generic_test

def merge_two_sorted_arrays(A, m, B, n):
    
    Ai, Bi = m - 1, n - 1
    for i in range(m + n - 1, -1, -1):
        if Ai < 0:
            A[i] = B[Bi]
            Bi -= 1
        elif Bi < 0:
            A[i] = A[Ai]
            Ai -= 1
        else:
            if A[Ai] >= B[Bi]:
                A[i] = A[Ai]
                Ai -= 1
            else:
                A[i] = B[Bi]
                Bi -= 1


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sorted_arrays_merge.py",
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
