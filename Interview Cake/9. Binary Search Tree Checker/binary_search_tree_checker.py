'''
	       5
	  3         7
	1   4     6   8
   x x|x x   x x|x x
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


#website solution
def checker2(root)
	return helper2(root, -float('inf'), float('inf'))

def helper2(node, rangeStart, rangeEnd):
	if not node:
		return True

	if node.val <= rangeStart or node.val >= rangeEnd:
		return False 
	
	return helper2(node.left, rangeStart, node.val) and helper2(node.right, node.val, rangeEnd)
