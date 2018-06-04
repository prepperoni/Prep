def hasCycle(head):
	slow = fast = head

	while fast.next and fast.next.next:
		slow = slow.next
		fast = fast.next.next

		if slow is fast:
			return True


	return False