# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/10/22 09:24 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : hard
"""
from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        satisfaction.sort()
        print(satisfaction)
        res = 0
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                dp[i][j] = dp[i - 1][j - 1] + satisfaction[i - 1] * j
                if j < i:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j])
                res = max(res, dp[i][j])
        return res


if __name__ == "__main__":
    sol = Solution()
    sol.maxSatisfaction([-1, -8, 0, 5, -9])
