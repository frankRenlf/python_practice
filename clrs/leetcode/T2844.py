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
        sum_val = 0
        k = 0
        while n != 0:
            if k % 2 == 0:
                sum_val += n % 10
            else:
                sum_val -= n % 10
            k += 1
            n //= 10
        return sum_val if k % 2 != 0 else -sum_val
