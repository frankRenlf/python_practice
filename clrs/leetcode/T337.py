# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/9/18 00:09 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import Optional

from clrs.leetcode.utils.TreeNode import TreeNode


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        res = self.dfs(root)
        return max(res)

    def dfs(self, root):
        if root is None:
            return [0, 0]
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        selected = root.val + l[1] + r[1]
        not_selected = max(l) + max(r)
        return [selected, not_selected]
# if __name__ == "__main__":
