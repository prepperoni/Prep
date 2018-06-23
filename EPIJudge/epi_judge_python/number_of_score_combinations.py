def num_combinations_for_final_score(final_score, individual_play_scores):
    memo = [0] * (final_score + 1)
    memo[0] = 1

    for x in individual_play_scores:
        for i in range(final_score + 1):
            if i + x <= final_score:
                memo[i + x] += memo[i]

    return memo[final_score]


from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
