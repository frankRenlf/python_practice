# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/7/14 10:45 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import Optional

from clrs.leetcode.utils.nodes import TreeNode


class Solution:
    move = 0

    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.move

    def dfs(self, root):
        moveleft = 0
        moveright = 0
        if root is None:
            return 0
        if root.left is not None:
            moveleft = self.dfs(root.left)
        if root.right is not None:
            moveright = self.dfs(root.right)
        self.move += abs(moveleft) + abs(moveright)
        return moveleft + moveright + root.val - 1
