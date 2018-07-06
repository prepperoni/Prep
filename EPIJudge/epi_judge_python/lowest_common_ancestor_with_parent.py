import functools
from sys import exit

from test_framework import generic_test, test_utils
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0, node1):
    def get_depth(node0):
        runner = node0
        depth = -1

        while runner:
            depth += 1
            runner = runner.parent

        return depth

    n0_depth, n1_depth = get_depth(node0), get_depth(node1)

    if n0_depth < n1_depth:
        node0, node1, n0_depth, n1_depth = node1, node0, n1_depth, n0_depth

    while n0_depth - n1_depth:
        node0, n0_depth = node0.parent, n0_depth - 1

    while node0:
        if node0 is node1:
            return node0
        node0, node1 = node0.parent, node1.parent

    return None


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.tsv',
                                       lca_wrapper))
