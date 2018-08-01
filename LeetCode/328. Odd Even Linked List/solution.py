# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def oddEvenList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    oddHead, evenHead = ListNode(None), ListNode(None)
    isOdd = True
    cur = head
    curOdd, curEven = oddHead, evenHead
    while cur:
        if isOdd:
            curOdd.next = cur
            curOdd = curOdd.next
        else:
            curEven.next = cur
            curEven = curEven.next
        isOdd = not isOdd
        cur = cur.next
    
    curOdd.next, curEven.next = None, None
    curOdd.next = evenHead.next
    
    return oddHead.next

head = ListNode(0)
tail = head
for i in range(1, 5):
    tail.next = ListNode(i)
    tail = tail.next

res = oddEvenList(head)

run = res

while run:
    print(run.val)
    run = run.next