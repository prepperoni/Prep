def intersect_two_sorted_arrays(A, B):
    Aidx = Bidx = 0
    res = []

    while Aidx < len(A) and Bidx < len(B):
    	if A[Aidx] == B[Bidx]:
    		if not res or A[Aidx] != res[-1]:
    			res.append(A[Aidx])
    		Aidx += 1
    		Bidx += 1
    	elif A[Aidx] < B[Bidx]:
    		Aidx += 1
    	else:
    		Bidx += 1 	

    return res


from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
