# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from clrs.leetcode.utils.nodes import TreeNode


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        self.elements = set([0])

        def dfs(node):
            if node is None:
                return
            if node.left:
                node.left.val = node.val * 2 + 1
                self.elements.add(node.left.val)
            if node.right:
                node.right.val = node.val * 2 + 2
                self.elements.add(node.right.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

    def find(self, target: int) -> bool:
        return target in self.elements


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
