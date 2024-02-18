# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/8/25 00:59 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""
from clrs.leetcode.utils.nodes import TreeNode


# if __name__ == "__main__":
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.sum_node(root, root.val)

    def sum_node(self, root, max_val):
        if root is None:
            return 0
        cnt = 0
        if root.val >= max_val:
            cnt += 1
            max_val = max(root.val, max_val)
        cnt += self.sum_node(root.left, max_val)
        cnt += self.sum_node(root.right, max_val)
        return cnt
