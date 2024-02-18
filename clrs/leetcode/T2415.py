# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/12/15 10:44 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
import queue
from typing import Optional

from clrs.leetcode.utils.nodes import TreeNode, create_perfect_binary_tree
from queue import Queue


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = Queue()
        q.put(root)
        depth = 0
        while not q.empty():
            n = q.qsize()
            arr = []
            while n > 0:
                n -= 1
                node = q.get()
                if depth % 2 != 0:
                    arr.append(node)
                if node.left is not None:
                    q.put(node.left)
                    q.put(node.right)
            if depth % 2 != 0:
                for i in range(len(arr) // 2):
                    tmp = arr[i].val
                    arr[i].val = arr[n - i - 1].val
                    arr[n - i - 1].val = tmp
            depth += 1
        return root


# 示例

if __name__ == "__main__":
    arr = [i for i in range(1, 16)]
    tree = create_perfect_binary_tree(arr)
    sol = Solution()
    sol.reverseOddLevels(tree)
    print(1)
