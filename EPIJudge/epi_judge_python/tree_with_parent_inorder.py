from test_framework import generic_test

'''
Elements of Programming Interviews in Python, problem 9.11 
Implement an inorder traversal with O(1) space (no recursion)

-nodes have parent pointers
-can't use explicit stack

sample tree:

			1
		2       3
	  4   5   6   7
     8 9

expected output: 8 4 9 2 5 1 6 3 7

'''


'''
ok let's see what this function below will return if we ran through that tree above

1. it'll keep traversing left until it hits node 8
2. output 8 because 8 has no left node. output so far: [8]
3. 8 has no right node, so next node is the parent of 8, which is 4
4. 8 is 4's left node, so the function adds 4 to the output. output so far [8, 4]
5. 4 does have a right node, which is 9
6. 9 does not have a left node, so add 9 to output. output is now [8, 4, 9]
7. 9 does not have a right node, so go to the parent, which is 4
8. 9 is 4's left node, so go to the parent, which is 2
9. 4 is 2's left node, so output 2. output: [8, 4, 9, 2]
...
yea it works accoring to the EPI judge too. So we're done.

'''
def inorder_traversal(tree): #without modifying the nodes this time
	prev = None #previously visited node
	next = None #node to visit next
	cur = tree
	output = []

	while cur:
		if prev is cur.parent:
			if cur.left:
				next = cur.left
			else:
				output.append(cur.data)
				next = cur.right if cur.right else cur.parent
		elif prev is cur.left:
			output.append(cur.data)
			next = cur.right if cur.right else cur.parent
		elif prev is cur.right:
			next = cur.parent

		prev = cur
		cur = next

	return output 


def inorder_traversal2(tree):
    cur = tree
    output = []
    while cur:
    	if cur.left and cur.left.data is not None: # hasn't visited left subtree
    		cur = cur.left # visit left subtree
    	elif cur.data is None: # definitely visted left subtree
    		if not cur.right or cur.right.data is None: # visited right subtree
    			cur = cur.parent
    		else:
    			cur = cur.right # visit right subtree
    	else:
    		output.append(cur.data)
    		cur.data = None

    return output


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_with_parent_inorder.py",
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
