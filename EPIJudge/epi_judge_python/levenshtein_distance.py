'''
A: bie 
B: pie

ie
pbie
pie
'''

def levenshtein_distance(A, B):
    def recurse(Ai, Bi):
        if memo[Ai][Bi] != -1:
            return memo[Ai][Bi]

        if Ai != len(A) and Bi != len(B):
            if A[Ai] == B[Bi]:
                memo[Ai][Bi] = recurse(Ai + 1, Bi + 1)
            else:
                memo[Ai][Bi] = 1 + min(recurse(Ai + 1, Bi), recurse(Ai, Bi + 1), recurse(Ai + 1, Bi + 1))
        else:
            if Ai == len(A):
                memo[Ai][Bi] = len(B) - Bi
            else:
                memo[Ai][Bi] = len(A) - Ai

        return memo[Ai][Bi]
    
    memo = [[-1] * (len(B) + 1) for _ in range(len(A) + 1)]
    memo[len(A)][len(B)] = 0
    recurse(0, 0)
    return memo[0][0]


from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("levenshtein_distance.tsv",
                                       levenshtein_distance))
