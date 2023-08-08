# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/8/8 09:44 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        p_pre, n_pre = 0, 0
        p_max, n_min = 0, 0
        res = 0
        for v in nums:
            p_pre = max(p_pre + v, v)
            p_max = max(p_max, p_pre)

            n_pre = min(n_pre + v, v)
            n_min = min(n_min, n_pre)
        return max(abs(p_max), abs(n_min))
