
import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items, capacity):
    memo = [[-1 for _ in range(capacity + 1)] for _ in range(len(items))]

    def fill(item_idx, remaining_cap):
    	if item_idx == len(items):
    		return 0 

    	if memo[item_idx][remaining_cap] == -1:
    		w, v = items[item_idx] #weight, value
	    	memo[item_idx][remaining_cap] = max(fill(item_idx + 1, remaining_cap), 0 if remaining_cap < w else v + fill(item_idx + 1, remaining_cap - w))
    	return memo[item_idx][remaining_cap]

    fill(0, capacity)
    return memo[0][capacity]

@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("knapsack.py", "knapsack.tsv",
                                       optimum_subject_to_capacity_wrapper))
