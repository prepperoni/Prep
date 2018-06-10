from heapq import heappush, heappop

def merge_sorted_arrays(sorted_arrays):
    res = []
    arrayCount = len(sorted_arrays)
    arrayIdicies = [0] * arrayCount
    heap = []
    #intialize heap with values from all arrays (arrVal, arrIndx)
    for i in range(arrayCount):
    	if sorted_arrays[i]:
    		heappush(heap, (sorted_arrays[i][0], i))

    #after popping, add the next item on that list if there is any
    while heap:
    	smallest = heappop(heap)
    	val, arrIdx = smallest
    	res.append(val)
    	arrayIdicies[arrIdx] += 1

    	if arrayIdicies[arrIdx] < len(sorted_arrays[arrIdx]):
    		heappush(heap, (sorted_arrays[arrIdx][arrayIdicies[arrIdx]], arrIdx))

    return res

def merge_sorted_arrays_easy(As):
	res = []

	for A in As:
		res.extend(A)

	res.sort()
	return res

from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
