'''
       5
  3         7
1   4     6   8
'''

def helper(node, vals):
	if not node:
		return
	helper(node.left, vals)
	vals.append(node.val)
	helper(node.right, vals)

def checker(root):
	vals = []

	helper(root, vals)

	for i in range(1, len(vals)):
		if vals[i] <= vals[i-1]:
			return False

	return True
