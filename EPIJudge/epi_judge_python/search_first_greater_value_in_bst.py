from sys import exit

from bst_node import BstNode
from test_framework import generic_test, test_utils

'''
         10
    3          17
  0    6    14     20
-1 1  5 7  13 15  19 21

'''

def find_first_greater_than_k(tree, k, first=True):
    res = None
    cur = tree

    while cur:
        if k >= cur.data:
            cur = cur.right
        else:
            res = cur
            cur = cur.left

    return res

def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_greater_value_in_bst.tsv',
                                       find_first_greater_than_k_wrapper))
