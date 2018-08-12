from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n):
    primes = []
    candidates = [True] * (n + 1)

    for i in range(2, n + 1):
    	if candidates[i]:
    		primes.append(i)
    		for j in range(i, n + 1, i):
    			candidates[j] = False

    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("prime_sieve.py", "prime_sieve.tsv",
                                       generate_primes))
