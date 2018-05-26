class Node:
	def __init__(val):
		self.val = val
		self.left = None
		self.right = None


#looks through every node (NOT OPTIMAL)
def secondLargset(root):
	maxVals = []
	helper(root, maxVals)
	return maxVals[1]

def helper(node, maxVals):
	if not node:
		return

	if node.val > maxVals[0]:
		maxVals[0] = [node.val, maxVals[0]]
	elif node.val > maxVals[1]:
		maxVals[1] = node.val

	if node.right:
		helper(node.right, maxVals)
	else:
		helper(node.left, maxVals)

#only looks through what is necessary
def secondLargest2(root):
	parent, largest = goRight(root)
	if largest != root and not largest.left:
		return parent

	return goRight(parent.left)[1].val

def goRight(node):
	preNode = Node(None)
	preNode.right = node
	while node.right:
		node = node.right
		preNode = node.right

	return [preNode, node]