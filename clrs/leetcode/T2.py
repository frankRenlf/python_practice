# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/7/2 08:51 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""
from typing import Optional

from clrs.leetcode.utils.ListNode import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_val = 0
        i = 1
        while l1 is not None:
            sum_val += l1.val * i
            i *= 10
            l1 = l1.next
        i = 1
        while l2 is not None:
            sum_val += l2.val * i
            i *= 10
            l2 = l2.next
        if sum_val == 0:
            return ListNode(0)
        pre = cur = ListNode(-1)
        while sum_val != 0:
            cur.next = ListNode(sum_val % 10)
            cur = cur.next
            sum_val /= 10
        return pre.next
