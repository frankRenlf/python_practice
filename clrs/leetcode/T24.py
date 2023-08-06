# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/8/6 10:49 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import Optional

from clrs.leetcode.utils.ListNode import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = prev = ListNode(-1)
        pre.next = head
        while pre.next and pre.next.next:
            n1 = pre.next
            n2 = n1.next
            n3 = n2.next
            pre.next = n2
            n2.next = n1
            n1.next = n3
            pre = pre.next
        return prev.next
