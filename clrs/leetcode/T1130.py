# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/5/31 20:02 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        stack = []
        for x in arr:
            while stack and stack[-1] <= x:
                y = stack.pop()
                if not stack or stack[-1] > x:
                    res += y * x
                else:
                    res += stack[-1] * y
            stack.append(x)
        while len(stack) >= 2:
            x = stack.pop()
            res += stack[-1] * x
        return res
