# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/8/20 00:33 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""
from typing import Optional

from clrs.leetcode.utils.TreeNode import TreeNode


# if __name__ == "__main__":

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def recall_sum(self, root):
        if root is None:
            return 0
        return root.val + self.recall_sum(root.left) + self.recall_sum(root.right)

    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == self.recall_sum(root.left) + self.recall_sum(root.right)
