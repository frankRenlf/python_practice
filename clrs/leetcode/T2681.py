# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/8/1 16:59 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : hard
"""
from typing import List


class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        nums.sort()
        dp = [0 for i in range(len(nums))]
        pre_sum = [0 for i in range(len(nums) + 1)]
        res, mod = 0, 10 ** 9 + 7
        for i in range(len(nums)):
            dp[i] = (nums[i] + pre_sum[i]) % mod
            pre_sum[i + 1] = (pre_sum[i] + nums[i] + pre_sum[i]) % mod
            res = (res + nums[i] * nums[i] * (nums[i] + pre_sum[i]) % mod) % mod
        return res
