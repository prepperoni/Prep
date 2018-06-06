def gcd(a, b):
	if not a:
		return b
	if not b:
		return a
	if a & 1 == 0 and b & 1 == 0:
		return gcd(a >> 1, b >> 1) << 1
	elif a & 1 == 1 and b & 1 == 1:
		return gcd(min(a, b), max(a, b) - min(a,b))
	else:
		if a & 1 == 0:
			a >>= 1
		if b & 1 == 0:
			b >>= 1
		return gcd(a, b)

def gcd_iterative(a, b):
	shift_count = 0
	while a and b:
		if a & 1 and b & 1:
			a, b = min(a, b), max(a, b) - min(a, b)
		else: 
			if not a & 1 and not b & 1:
				shift_count += 1
			if not a & 1:
				a >>= 1
			if not b & 1:
				b >>= 1

	return a << shift_count if a else b << shift_count

from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(generic_test.generic_test_main('gcd.tsv', gcd))
