def count_bits(x):
    # Implement this placeholder.
    count = 0

    while x: 
    	count += 1
    	x = (x-1)&x

    return count


from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(generic_test.generic_test_main('count_bits.tsv', count_bits))
