#recursive
def findMinMaxPaths(node, curHeight, minMax):
	if not node:
		minMax[0] = min(minMax[0], curHeight)
		minMax[1] = max(minMax[1], curHeight)
	else:
		super_balanced(node.left, curHeight + 1, minMax)
		super_balanced(node.right, curHeight + 1, minMax)


def isSuperbalanced(root):
	minMax = (-float('inf'), float('inf'))
	findMinMaxPaths(root, 0, minMax)

	return minMax[1] - minMax[0] <= 1

#iterative
def isSuperbalanced(root):
	layer = 0
	firstLeafLayer = None
	q1, q2 = queue.Queue(), queue.Queue()
	q.put(root)

	while not q1.empty():
		cur = q1.get()

		if not cur.left and not cur.right and not firstLeafLayer:
			firstLeafLayer = layer

		if cur.left:
			q2.put(cur.left)
		if cur.right:
			q2.put(cur.right)

		if q1.empty() and not q2.empty():
			q1, q2 = q2, q1
			layer += 1
			if firstLeafLayer and layer - firstLeafLayer > 1:
				return False

	return True