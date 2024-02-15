# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

from clrs.leetcode.utils.TreeNode import TreeNode
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans
        q = deque()
        q.append(root)
        depth = 0
        while len(q):
            l = len(q)
            cur = []
            while l:
                node = q.popleft()
                cur.append(node.val)
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
                l -= 1
            if depth % 2 != 0:
                cur.reverse()
            ans.append(cur)
            depth += 1
        return ans
