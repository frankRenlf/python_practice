# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/5/30 23:18 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import Optional, List

from clrs.leetcode.utils.Node import TreeNode


class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        roots = []
        self.dfs(root, True, to_delete_set, roots)
        return roots

    def dfs(
        self,
        node: Optional[TreeNode],
        is_root: bool,
        to_delete_set: set[int],
        roots: List[TreeNode],
    ) -> Optional[TreeNode]:
        if node is None:
            return None
        delete = node.val in to_delete_set
        node.left = self.dfs(node.left, delete, to_delete_set, roots)
        node.right = self.dfs(node.right, delete, to_delete_set, roots)
        if delete:
            return None
        else:
            if is_root:
                roots.append(node)
            return node
