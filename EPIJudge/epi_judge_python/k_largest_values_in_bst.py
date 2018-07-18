def find_k_largest_in_bst(tree, k):
    def helper(tree):
    	if not tree or len(klargest) == k:
    		return
    	helper(tree.right)
    	if len(klargest) < k:
    		klargest.append(tree.data)
    	helper(tree.left)

    klargest = []
    helper(tree)
    return klargest



from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
