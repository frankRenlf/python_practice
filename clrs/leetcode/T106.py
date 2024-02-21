from typing import List, Optional

from clrs.leetcode.utils.nodes import TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def myBuildTree(
            postorder_left: int,
            postorder_right: int,
            inorder_left: int,
            inorder_right: int,
        ):
            if postorder_left > postorder_right:
                return None

            preorder_root = postorder_right
            inorder_root = index[postorder[preorder_root]]

            root = TreeNode(postorder[preorder_root])

            size_right_subtree = inorder_right - inorder_root

            root.right = myBuildTree(
                postorder_right - size_right_subtree,
                postorder_right - 1,
                inorder_root + 1,
                inorder_right,
            )

            root.left = myBuildTree(
                postorder_left,
                postorder_right - size_right_subtree - 1,
                inorder_left,
                inorder_root - 1,
            )

            return root

        n = len(postorder)
        # 构造哈希映射，帮助我们快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)
