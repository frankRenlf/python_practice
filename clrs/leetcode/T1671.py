# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/12/22 09:25 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : hard
"""
from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        pre = self.getLISArray(nums)
        suf = self.getLISArray(nums[::-1])[::-1]
        ans = 0

        for pre_i, suf_i in zip(pre, suf):
            if pre_i > 1 and suf_i > 1:
                ans = max(ans, pre_i + suf_i - 1)

        return len(nums) - ans

    def getLISArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp

# if __name__ == "__main__":
