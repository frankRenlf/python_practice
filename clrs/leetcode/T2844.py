# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/7/12 10:22 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : easy
"""


class Solution:
    def alternateDigitSum(self, n: int) -> int:
        res = 0
        while n > 0:
            res = n % 10 - res
            n //= 10
        return res
