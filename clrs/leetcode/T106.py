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

            # 前序遍历中的第一个节点就是根节点
            preorder_root = postorder_right
            # 在中序遍历中定位根节点
            inorder_root = index[postorder[preorder_root]]

            # 先把根节点建立出来
            root = TreeNode(postorder[preorder_root])

            # 得到左子树中的节点数目
            size_right_subtree = inorder_right - inorder_root
            # 递归地构造右子树，并连接到根节点
            # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right = myBuildTree(
                postorder_right - size_right_subtree,
                postorder_right - 1,
                inorder_root + 1,
                inorder_right,
            )

            # 递归地构造左子树，并连接到根节点
            # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
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
