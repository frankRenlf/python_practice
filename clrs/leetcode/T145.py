from typing import Optional, List

from clrs.leetcode.utils.nodes import TreeNode


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def postorder(node):
            if node is None:
                return
            postorder(node.left)

            postorder(node.right)
            res.append(node.val)

        postorder(root)
        return res
