from test_framework import generic_test


def next_permutation(perm):
    pivot_idx = -1
    for i in range(len(perm) - 1, 0, -1):
        if perm[i] > perm[i - 1]:
            pivot_idx = i - 1
            break

    if pivot_idx == -1:
        return []

    for j in range(len(perm) - 1, pivot_idx, -1):
        if perm[j] > perm[pivot_idx]:
            perm[j], perm[pivot_idx] = perm[pivot_idx], perm[j]
            break

    perm[pivot_idx + 1:] = perm[pivot_idx + 1:][::-1]

    return perm


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "next_permutation.py", 'next_permutation.tsv', next_permutation))
