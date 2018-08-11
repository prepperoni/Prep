from test_framework import generic_test

#problem 4.3 on EPI python
#reverse bits of a 64-bit word
# x          1100101
# left mask  1000000
# right mask 0000001
def reverse_bits(x):
    for i in range(32):
    	# if the bit values are different
    	if (x >> (63 - i)) & 1 != ((x >> i) & 1):
    		#swap the two bit values -> invert their values
    		x ^= (1 << i) | (1 << 63 - i)

    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_bits.py", "reverse_bits.tsv",
                                       reverse_bits))
