from test_framework import generic_test, test_utils


def permutations(A):
    if not A:
        return []
    elif len(A) == 1:
        return [A]

    res = []
    subperms = permutations(A[:len(A) - 1])
    for s in subperms:
        s.append(A[-1])
        for i in range(len(s)):
            s[i], s[-1] = s[-1], s[i]
            res.append(list(s))
            s[i], s[-1] = s[-1], s[i]
    return res

#book solution
def permutations(A):
    res = []
    def recurse(idx):
        if idx == len(A):
            res.append(list(A)) 

        for i in range(idx, len(A)):
            A[idx], A[i] = A[i], A[idx]
            recurse(idx + 1)
            A[idx], A[i] = A[i], A[idx]

    recurse(0)
    return res
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("permutations.py", 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
