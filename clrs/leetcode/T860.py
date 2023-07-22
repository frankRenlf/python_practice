# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/7/22 09:54 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : easy
"""
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d_map = {}
        base = 5
        for v in bills:
            if v == base:
                d_map[v] += 1
            else:
                sub = v - base
                k = sub / 5
                while k > 1:
                    val = k * 5
                    if d_map[val] > 0:
                        d_map[val] -= 1
                        sub = 0
                    else:
                        k -= 1


class Solution2:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for v in bills:
            if v == 5:
                five += 1
            elif v == 10:
                ten += 1
                five -= 1
            else:
                if ten:
                    ten -= 1
                    five -= 1
                else:
                    five -= 3
            if five < 0:
                return False
        return True
