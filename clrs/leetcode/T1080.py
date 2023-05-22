# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/5/22 08:26 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description :
"""
from typing import Optional

from clrs.leetcode.utils.TreeNode import TreeNode


class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        res = self.dfs(root, 0, limit)
        return root if res else None

    def dfs(self, node, pre, limit):
        if node is None:
            return False
        if node.left is None and node.right is None:
            return node.val + pre >= limit
        cur = pre + node.val
        left_sum = self.dfs(node.left, cur, limit)
        right_sum = self.dfs(node.right, cur, limit)
        if not left_sum:
            node.left = None
        if not right_sum:
            node.right = None
        return left_sum or right_sum
