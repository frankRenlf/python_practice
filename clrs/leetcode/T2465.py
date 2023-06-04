# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/6/4 08:44 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description :
"""
from typing import List


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        cpy = set()
        n = len(nums)
        for i in range(n // 2):
            val = (nums[i] + nums[n - i - 1])
            cpy.add(val)
        return len(cpy)
