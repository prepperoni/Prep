from test_framework import generic_test
from list_node import ListNode

def even_odd_merge(L):
    even_head, odd_head = ListNode(), ListNode()
    even_tail, odd_tail = even_head, odd_head
    cur = L
    isEven = False

    while cur:
    	if isEven:
    		even_tail.next = cur
    		even_tail = even_tail.next
    	else:
    		odd_tail.next = cur
    		odd_tail = odd_tail.next

    	cur = cur.next
    	isEven = not isEven

    even_tail.next = None
    odd_tail.next = even_head.next

    return odd_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("even_odd_list_merge.py",
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
