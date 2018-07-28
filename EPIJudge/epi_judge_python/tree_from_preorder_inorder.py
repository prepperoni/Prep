from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def binary_tree_from_preorder_inorder(preorder, inorder):
    def recurse(istart, iend, pstart, pend):
        head_val = preorder[pstart]
        new_node = BinaryTreeNode(head_val)
        head_idx = i_val_to_idx[head_val]
        left_len = head_idx - istart

        if istart < head_idx:
            new_node.left = recurse(istart, head_idx - 1, pstart + 1, pstart + left_len)
        if iend > head_idx:
            new_node.right = recurse(head_idx + 1, iend, pstart + left_len + 1, pend)

        return new_node
    i_val_to_idx = {}

    for i,v in enumerate(inorder):
        i_val_to_idx[v] = i

    return None if not inorder else recurse(0, len(inorder) - 1, 0, len(inorder) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))

