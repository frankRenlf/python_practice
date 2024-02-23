# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from utils.nodes import TreeNode

from queue import PriorityQueue
from collections import deque


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = deque()
        q.append(root)

        ql = PriorityQueue()

        while q:
            l = len(q)
            layer = 0
            while l:
                node = q.popleft()
                layer -= node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                l -= 1
            ql.put(layer)
        ans = 0
        while k and not ql.empty():
            ans = -ql.get()
            k -= 1
        return -1 if k > 0 else ans


if __name__ == "__main__":
    k = 2
    ql = PriorityQueue()
    ql.put(2)
    while k and ql:
        ans = -ql.get()
        k -= 1
