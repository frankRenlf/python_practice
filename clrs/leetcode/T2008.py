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
from bisect import bisect_right
from typing import List


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort(key=lambda x: x[1])
        cnt = len(rides)
        dp = [0] * (n + 1)
        index = 0
        for i in range(1, n + 1):
            if index < cnt and rides[index][1] == i:
                mx = 0
                while index < cnt and rides[index][1] == i:
                    mx = max(mx, (dp[rides[index][0]] + rides[index][1]
                                  - rides[index][0] + rides[index][2]))
                    index += 1
                dp[i] = max(dp[i - 1], mx)
            else:
                dp[i] = dp[i - 1]
        return dp[n]

    def maxTaxiEarnings_optim(self, n: int, rides: List[List[int]]) -> int:
        rides.sort(key=lambda r: r[1])
        m = len(rides)
        dp = [0] * (m + 1)
        for i in range(m):
            j = bisect_right(rides, rides[i][0], hi=i, key=lambda r: r[1])
            dp[i + 1] = max(dp[i], dp[j] + rides[i][1] - rides[i][0] + rides[i][2])
        return dp[m]


if __name__ == "__main__":
    sol = Solution()
    sol.maxTaxiEarnings(
        n=20, rides=[[1, 6, 1], [3, 10, 2], [10, 12, 3], [11, 12, 2], [12, 15, 2], [13, 18, 1]]
    )
