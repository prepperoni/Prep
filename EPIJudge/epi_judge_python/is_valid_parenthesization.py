from test_framework import generic_test


def is_well_formed(s):
    stk = []
    mapping = {'(':')', '[':']', '{':'}'}

    for c in s:
    	if c in '([{':
    		stk.append(c)
    	else:
    		if not stk or mapping[stk[-1]] != c:
    			return False
    		stk.pop()

    return not stk


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_parenthesization.py",
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
