# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/12/4 11:16 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from clrs.leetcode.utils.TreeNode import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.prefix = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node is None:
                return
            inorder(node.right)
            self.prefix += node.val
            node.val = self.prefix
            inorder(node.left)

        inorder(root)
        return root


if __name__ == "__main__":
    root0 = TreeNode(0)

    root0.right = root = TreeNode(2)
    root.right = TreeNode(3)
    root.left = TreeNode(1)
    sol = Solution()
    sol.bstToGst(root0)
    print(root0)
