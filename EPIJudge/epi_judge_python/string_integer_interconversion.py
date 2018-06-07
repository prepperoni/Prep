from sys import exit

from test_framework import generic_test, test_utils
from test_framework.test_failure import TestFailure


def int_to_string(x):
    result = []
    is_negative = False
    
    if x < 0:
        is_negative = True
        x = -x

    if x == 0:
        return '0'

    while x:
        result.append(chr(ord('0') + x%10))
        x //= 10

    if is_negative:
        result.append('-')

    result.reverse()

    return ''.join(result)


def string_to_int(s):
    is_negative = False
    if s[0] == '-':
        is_negative = True
        s = s[1:]

    res = 0

    for digit in s:
        res *= 10
        res += ord(digit) - ord('0') 

    if is_negative:
        res = -res

    return res

def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.tsv',
                                       wrapper))
