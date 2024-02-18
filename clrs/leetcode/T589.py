from typing import List
from clrs.leetcode.utils.nodes import Node


class Solution:
    def preorder(self, root: "Node") -> List[int]:
        ans = []

        def dfs(node):
            if node == None:
                return
            ans.append(node.val)
            for child in node.children:
                dfs(child)

        dfs(root)
        return ans
