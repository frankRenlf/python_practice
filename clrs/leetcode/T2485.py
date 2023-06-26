# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/6/26 08:38 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : easy
"""


class Solution:
    def pivotInteger(self, n: int) -> int:
        left = 0
        right = sum(i for i in range(n + 1))
        pos = -1
        for i in range(1, n + 1):
            left += i
            right -= i - 1
            if left >= right:
                pos = i
                break
        return pos if left == right else -1
