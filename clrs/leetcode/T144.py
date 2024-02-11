from typing import Optional, List

from clrs.leetcode.utils.TreeNode import TreeNode


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(node):
            if node is None:
                return
            res.append(node.val)
            inorder(node.left)

            inorder(node.right)

        inorder(root)
        return res
