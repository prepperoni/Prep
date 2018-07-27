from test_framework import generic_test


def is_symmetric(tree):
    def sym(n1, n2):
    	print("called")
    	if not n1 and not n2:
    		return True
    	return (n1 is not None and n2 is not None) and (n1.data == n2.data) and sym(n1.left, n2.right) and sym(n1.right, n2.left)

    if not tree:
    	return True

    return sym(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
