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

from clrs.leetcode.utils.nodes import TreeNode


class Solution:
    def sufficientSubset(
        self, root: Optional[TreeNode], limit: int
    ) -> Optional[TreeNode]:
        res = self.dfs(root, 0, limit)
        return root if res >= limit else None

    def dfs(self, node, pre, limit):
        if node is None:
            return -float("inf")
        if node.left is None and node.right is None:
            return node.val + pre
        cur = pre + node.val
        left_sum = self.dfs(node.left, cur, limit)
        right_sum = self.dfs(node.right, cur, limit)
        if left_sum < limit:
            node.left = None
        if right_sum < limit:
            node.right = None
        res = max(left_sum, right_sum)
        return res

    def sufficientSubset2(
        self, root: Optional[TreeNode], limit: int
    ) -> Optional[TreeNode]:
        res = self.dfs(root, 0, limit)
        return root if res else None

    def dfs2(self, node, pre, limit):
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
