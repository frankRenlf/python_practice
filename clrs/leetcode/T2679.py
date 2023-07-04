# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/7/4 09:55 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        res = 0
        m, n = len(nums), len(nums[0])
        for i in range(m):
            nums[i].sort()
        for j in range(n):
            max_val = 0
            for i in range(m):
                max_val = max(max_val, nums[i][j])
            res += max_val
        return res
