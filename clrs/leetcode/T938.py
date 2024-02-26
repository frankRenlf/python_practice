# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from clrs.leetcode.utils.nodes import TreeNode


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        if root == None:
            return 0
        if low <= root.val <= high:
            ans += root.val
        if high >= root.val:
            ans += self.rangeSumBST(root.right, low, high)
        if low <= root.val:
            ans += self.rangeSumBST(root.left, low, high)

        return ans
