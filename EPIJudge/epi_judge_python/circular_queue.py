from test_framework import generic_test
from test_framework.test_failure import TestFailure

'''
Problem 8.8 Implement a Circular Queue

'''

class Queue:
    def __init__(self, capacity):
        # underlying array/list
        self.A = [None for _ in range(capacity)]
        self.head_idx = 0
        self.tail_idx = 0
        self.length = 0 #number of elements in the queue, not A

    def enqueue(self, x):
        if self.length == len(self.A):
            self.A = self.A[self.head_idx:] + self.A[:self.head_idx]
            self.head_idx, self.tail_idx = 0, len(self.A)
            self.A = self.A + [None for _ in range(len(self.A))]

        self.A[self.tail_idx] = x

        if self.tail_idx == len(self.A) - 1:
            self.tail_idx = 0
        else:
            self.tail_idx += 1
        
        self.length += 1

    def dequeue(self):
        val = self.A[self.head_idx]
        if self.head_idx == len(self.A) - 1:
            self.head_idx = 0
        else:
            self.head_idx += 1
        self.length -= 1
        return val

    def size(self):
        return self.length



















def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure(
                    "Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("circular_queue.py",
                                       'circular_queue.tsv', queue_tester))
