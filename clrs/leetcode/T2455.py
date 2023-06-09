# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/5/29 08:49 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : easy
"""
from typing import List


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sum_val = 0
        cnt = 0
        for i in nums:
            if i % 6 == 0:
                sum_val += i
                cnt += 1
        return sum_val // cnt if cnt > 0 else 0
