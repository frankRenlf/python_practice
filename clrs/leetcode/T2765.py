# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2024/1/23 08:35 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : easy
"""
from typing import List


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        res = -1
        firstIndex = 0
        for i in range(1, len(nums)):
            length = i - firstIndex + 1
            if nums[i] - nums[firstIndex] == (length - 1) % 2:
                res = max(res, length)
            else:
                if nums[i] - nums[i - 1] == 1:
                    firstIndex = i - 1
                    res = max(res, 2)
                else:
                    firstIndex = i
        return res

    def alternatingSubarray_dp(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        cur = 1
        for i in range(1, n):
            if nums[i] - nums[i - 1] == cur:
                dp[i] = dp[i - 1] + 1
                cur *= -1
            elif nums[i] - nums[i - 1] == 1:
                dp[i] = 2
                cur = -1
            else:
                cur = 1
        res = max(dp)
        return -1 if res <= 1 else res
# if __name__ == "__main__":
