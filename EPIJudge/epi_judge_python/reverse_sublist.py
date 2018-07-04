from sys import exit

from list_node import ListNode
from test_framework import generic_test, test_utils


def reverse_sublist(L, start, finish):
	if start == finish:
		return L

	fakehead = pre = ListNode(None, L)
	dist = finish - start

	while (start - 1):
		pre = pre.next
		start -= 1

	post = pre.next

	while dist:
		dist -= 1 
		toSwap = post.next
		post.next = toSwap.next
		toSwap.next = pre.next
		pre.next = toSwap

	return fakehead.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.tsv", reverse_sublist))
