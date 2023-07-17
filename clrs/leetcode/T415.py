# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/7/17 09:05 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : easy
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        n1, n2 = len(num1) - 1, len(num2) - 1
        carry = 0
        while n1 >= 0 or n2 >= 0 or carry != 0:
            p1 = int(num1[n1]) if n1 >= 0 else 0
            p2 = int(num2[n2]) if n2 >= 0 else 0
            sum_val = p1 + p2 + carry
            res = str(sum_val % 10) + res
            carry = sum_val // 10
            n1 -= 1
            n2 -= 1
        return res
