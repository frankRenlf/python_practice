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
        n = len(nums)
        dp = [0] * n
        pre_sum = 0
        res, mod = 0, 10 ** 9 + 7
        for i in range(n):
            dp[i] = (nums[i] + pre_sum) % mod
            pre_sum = (pre_sum + dp[i]) % mod
            res = (res + nums[i] * nums[i] * dp[i]) % mod
        return res
