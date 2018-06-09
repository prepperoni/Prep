from sys import exit

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test, test_utils


def is_balanced_binary_tree(tree):
    def helper(node):
    	if not node:
    		return (True, -1)

    	left_status = helper(node.left)
    	if not left_status[0]:
    		return (False, 0)

    	right_status = helper(node.right)
    	if not right_status[0]:
    		return (False, 0)

    	height = max(left_status[1], right_status[1]) + 1
    	balanced = abs(left_status[1] - right_status[1]) <= 1
    	return (balanced, height)

    return helper(tree)[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.tsv',
                                       is_balanced_binary_tree))