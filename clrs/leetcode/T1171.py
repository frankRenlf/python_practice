# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/6/11 00:26 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""
from typing import Optional

from clrs.leetcode.utils.ListNode import ListNode


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(0)
        prev.next = head
        prefix = 0
        dict_ = {prefix: prev}
        while head is not None:
            prefix += head.val
            dict_[prefix] = head
            head = head.next

        prefix = 0
        head = prev
        while head is not None:
            prefix += head.val
            head.next = dict_[prefix].next
            head = head.next
        return prev.next
