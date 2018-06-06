def parity(x):
    known_parities = {}
    parity_sum = 0

    while x:
    	some_bits = x & 0xffff
    	if some_bits not in known_parities:
    		known_parities[some_bits] = parityMini(some_bits)
    	parity_sum += known_parities[some_bits]
    	x >>= 16

    return parity_sum % 2

def parityMini(x):
	ones = 0

	while x:
		ones += 1
		x = x & (x - 1)

	return ones % 2
	
def lognparity(x):
	x ^= x >> 32
	x ^= x >> 16
	x ^= x >> 8
	x ^= x >> 4
	x ^= x >> 2
	x ^= x >> 1

	return x & 1

from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.tsv', parity))
