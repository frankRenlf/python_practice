# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/11/3 09:20 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
import queue


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        cur = root
        while cur is not None:
            dummy = Node(-1)
            pre = dummy
            while cur is not None:
                if cur.left is not None:
                    pre.next = cur.left
                    pre = pre.next
                if cur.right is not None:
                    pre.next = cur.right
                    pre = pre.right
                cur = cur.next
            cur = dummy.next
        return root


if __name__ == "__main__":
    sol = Solution()
    sol.connect()
