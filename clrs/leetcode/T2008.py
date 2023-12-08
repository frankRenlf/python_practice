# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/12/8 08:31 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort(key=lambda x: x[1])
        dp = [0] * (n + 1)
        for r in rides:
            dp[r[1]] += dp[r[0]] + dp[r[1]] - dp[r[0]] + r[2]


if __name__ == "__main__":
    sol = Solution()
    sol.maxTaxiEarnings(n=20, rides=[[1, 6, 1], [3, 10, 2], [10, 12, 3], [11, 12, 2], [12, 15, 2], [13, 18, 1]])
