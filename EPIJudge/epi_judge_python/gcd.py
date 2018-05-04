def gcd(a, b):
	if a == b:
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


from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(generic_test.generic_test_main('gcd.tsv', gcd))
