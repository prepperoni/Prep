import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(tree, node0, node1):
  def call_stk(curNode, key, stk):

    if curNode is None:
      return None

    stk.append(curNode)
    
    if curNode is key:
      return stk

    left_res = call_stk(curNode.left, key, stk)
    if left_res:
      return left_res

    right_res = call_stk(curNode.right, key, stk)
    if right_res:
      return right_res

    stk.pop()

  n0_stk = call_stk(tree, node0, [])
  n1_stk = call_stk(tree, node1, [])

  res = None
  for i in range(min(len(n0_stk), len(n1_stk))):
    if n0_stk[i] is n1_stk[i]:
      res = n0_stk[i]

  return res


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
