from test_framework import generic_test
from heapq import *

'''
Problem 10.5 of Elements of Programming Interviews in Python -- Compute the median of online data. 
Aka, find the medians of a stream of numbers

My own example: say the stream is 3 1 4 1 5 9 2 6 5

medians would be 3, then (3 + 1) / 2, then 3, then the median of 1 1 2 3, which is (1 + 2) / 2, and so on

Brute force: keep a sorted list of the number encountered so far, and each time you get a new number, add it to the sorted list
             each insertion would be O(n). For N numbers in the sequence, that would lead to an O(N^2) algo.

Better solution: What if keep two data structures -- one containing the larger half of numbers encountered so far, and one 
                 containing the smaller half? These two data structures would be a max heap of the smaller half, and a 
                 min heap of the larger half -- giving you quick access to the median value(s)

5 4 3 2 1

max[5]
min[]

max[4]
min[-5]

'''
def online_median(sequence):
    medians = []
    max_h, min_h = [], []

    for s in sequence:
    	heappush(max_h, -s)
    	heappush(min_h, -heappop(max_h))

    	if len(min_h) > len(max_h):
    		heappush(max_h, -heappop(min_h))

    	if len(max_h) > len(min_h):
    		medians.append(-max_h[0])
    	else:
    		medians.append((-max_h[0] + min_h[0]) / 2)

    return medians

    # for s in sequence:
    # 	if not max_h or s <= -max_h[0]:
    # 		heappush(max_h, -s)
    # 	else:
    # 		heappush(min_h, s)

    # 	if len(max_h) - len(min_h) == 2:
    # 		heappush(min_h, -heappop(max_h))
    # 	elif len(min_h) - len(max_h) == 2:
    # 		heappush(max_h, -heappop(min_h))

    # 	if len(max_h) > len(min_h):
    # 		medians.append(-max_h[0])
    # 	elif len(max_h) < len(min_h):
    # 		medians.append(min_h[0])
    # 	else:
    # 		medians.append((-max_h[0] + min_h[0]) / 2)

    # return medians



































def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("online_median.py", "online_median.tsv",
                                       online_median_wrapper))
