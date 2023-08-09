# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/8/9 10:04 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : easy
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul = 1
        add = 0
        while n:
            cur = n % 10
            mul *= cur
            add += cur
            n //= 10
        return mul - add
