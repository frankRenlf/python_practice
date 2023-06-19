# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/6/19 22:54 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        f = [0, -float("inf"), -float("inf")]
        for num in nums:
            g = f[:]
            for i in range(3):
                g[(i + num % 3) % 3] = max(g[(i + num % 3) % 3], f[i] + num)
            f = g
        return f[0]
