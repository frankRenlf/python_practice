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
    def __int__(self, is_bst, min_val, max_val, sum_val):
        self.is_bst = is_bst
        self.min_val = min_val
        self.max_val = max_val
        self.sum_val = sum_val


class Solution:
    INF = 0x3f3f3f3f

    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if root is None:
            return SubTree(True, self.INF, -self.INF, 0)
