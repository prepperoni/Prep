def find_k_largest_in_bst(tree, k):
    def helper(tree, k, klargest):
    	if not tree:
    		return
    	helper(tree.right, k, klargest)
    	if len(klargest) < k:
    		klargest.append(tree.data)
    	helper(tree.left, k, klargest)

    klist = []
    helper(tree, k, klist)
    return klist



from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
