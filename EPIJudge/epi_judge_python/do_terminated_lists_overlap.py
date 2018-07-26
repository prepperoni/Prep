import functools
from sys import exit

from test_framework import generic_test, test_utils
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0, l1):
    def list_len(head):
        length = 0
        head_ = head

        while head_:
            length += 1
            head_ = head_.next

        return length

    l0_len, l1_len = list_len(l0), list_len(l1)

    if l1_len > l0_len:
        l0, l1 = l1, l0

    l0_node = l0

    for _ in range(abs(l0_len - l1_len)):
        l0_node = l0_node.next

    l1_node = l1
    while l0_node:
        if l0_node == l1_node:
            return l0_node
        l0_node, l1_node = l0_node.next, l1_node.next

    return None


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(
        functools.partial(overlapping_no_cycle_lists, l0, l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
