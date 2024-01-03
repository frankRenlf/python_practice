# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2024/1/3 10:04 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : 
"""
from typing import Optional

from clrs.leetcode.utils.ListNode import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        st = []
        while head is not None:
            st.append(head)
            head = head.next
        root = None
        while st:
            if root is None or st[-1].val >= root.val:
                st[-1].next = root
                root = st[-1]
            st.pop()
        return root

# if __name__ == "__main__":
