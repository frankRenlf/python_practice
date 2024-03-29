from ast import List
from bisect import bisect_left
from typing import Optional

from clrs.leetcode.utils.nodes import TreeNode


class Solution:
    def closestNodes(
        self, root: Optional[TreeNode], queries: List[int]
    ) -> List[List[int]]:
        arr = []

        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)

        dfs(root)
        res = []
        for val in queries:
            maxVal, minVal = -1, -1
            index = bisect_left(arr, val)
            if index != len(arr):
                maxVal = arr[index]
                if arr[index] == val:
                    minVal = arr[index]
                    res.append([minVal, maxVal])
                    continue
            if index != 0:
                minVal = arr[index - 1]
            res.append([minVal, maxVal])
        return res
