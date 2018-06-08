from sys import exit

from list_node import ListNode
from test_framework import generic_test, test_utils


def merge_two_sorted_lists(L1, L2):
    temp_head = slow = ListNode(None)
    slow.next = L1

    while L2:
    	if L1 and L1.data <= L2.data:
    		L1 = L1.next
    		slow = slow.next
    	else:
    		temp = L2
    		L2 = L2.next
    		temp.next = L1
    		slow.next = temp
    		L1 = temp

    return temp_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
