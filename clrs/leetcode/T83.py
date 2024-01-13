# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2024/1/14 00:04 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : easy
"""
from typing import Optional

from clrs.leetcode.utils.ListNode import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101)
        dummy.next = head
        slow = fast = head
        while fast is not None:
            while fast is not None and slow.val == fast.val:
                fast = fast.next
            slow.next = fast
            slow = slow.next
        return dummy.next

# if __name__ == "__main__":
