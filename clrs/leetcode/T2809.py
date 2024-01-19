# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2024/1/19 09:52 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : hard
"""
from typing import List


class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        n = len(nums1)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for j, (b, a) in enumerate(sorted(zip(nums2, nums1)), 1):
            for i in range(j, 0, -1):
                dp[j][i] = max(dp[j - 1][i], dp[j - 1][i - 1] + i * b + a)
        sa, sb = sum(nums1), sum(nums2)
        for i in range(0, n + 1):
            if sb * i + sa - dp[n][i] <= x:
                return i
        return -1

# if __name__ == "__main__":
