def reverseRecursive(node):
	if node.next:
		new_head = reverseRecursive(node.next)
		node.next.next = node
		node.next = None
		return new_head
	return node

def reverseIterative(head):
	cur = node
	prev = None

	while cur:
		next_node = cur.next
		cur.next = prev
		prev = cur
		cur = next_node

	return prev