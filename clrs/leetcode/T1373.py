# -*- coding: UTF-8 -*-
"""
@Project : python_practice 
@env     : PyCharm
@File    : T1373.py
@Author  : Frank
@Date    : 2023/5/20 08:02 
"""
from typing import Optional

from clrs.leetcode.utils.TreeNode import TreeNode


class SubTree:
    def __init__(self, is_bst, min_val, max_val, sum_val):
        self.is_bst = is_bst
        self.min_val = min_val
        self.max_val = max_val
        self.sum_val = sum_val


class Solution:
    INF = 0x3f3f3f3f

    def __init__(self):
        self.res = 0

    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if root is None:
            return SubTree(True, self.INF, -self.INF, 0)
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if left.is_bst and right.is_bst and left.max_val < root.val < right.min_val:
            cur_sum_val = root.val + left.sum_val + right.sum_val
            self.res = max(self.res, cur_sum_val)
            return SubTree(True, min(root.val, left.min_val), max(root.val, right.max_val), cur_sum_val)
        return SubTree(False, 0, 0, 0)
