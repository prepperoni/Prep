# Uses BFS to find the least steps of transformation.
def transform_string(D, s, t):
    steps = 0
    current_set = {s}

    while current_set:
        next_set = set()
        
        for cur_word in current_set:
            if cur_word == t:
                return steps

            for c in "abcdefghijklmnopqrstuvwxyz":
                for i in range(len(s)):
                    candidate = cur_word[:i] + c + cur_word[i+1:]
                    if candidate in D:
                        D.discard(candidate)
                        next_set.add(candidate)

        steps += 1
        current_set = next_set

    return -1


from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_transformability.tsv',
                                       transform_string))
