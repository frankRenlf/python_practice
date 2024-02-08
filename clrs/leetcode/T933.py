# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from utils.TreeNode import TreeNode
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        