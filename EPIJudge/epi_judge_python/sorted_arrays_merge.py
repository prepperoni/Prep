from heapq import heappush, heappop

def merge_sorted_arrays(sorted_arrays):
    res = []
    heap = []
    iterators = [iter(x) for x in sorted_arrays]
    #intialize heap with values from all arrays (arrVal, arrIndx)
    for arrIdx, iterator in enumerate(iterators):
    	val = next(iterator, None)
    	if val is not None:
    		heappush(heap, (val, arrIdx))

    #after popping, add the next item on that list if there is any
    while heap:
    	smallest = heappop(heap)
    	val, arrIdx = smallest
    	res.append(val)
    	nextVal = next(iterators[arrIdx], None)

    	if nextVal is not None:
    		heappush(heap, (nextVal, arrIdx))

    return res

#print(merge_sorted_arrays([[1,2,3], [4,5,6]]))

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
