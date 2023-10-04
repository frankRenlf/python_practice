# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/10/4 09:38 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : hard
"""
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        num = min(k, n // 2)
        dp = [[[0] * (num + 1) for _ in range(2)] for _ in range(n)]
        # i,buy or sell, num
        dp[0][0][0] = -prices[0]
        dp[0][1][0] = 0
        for i in range(1, num + 1):
            dp[0][0][i] = dp[0][1][i] = float("-inf")

        for i in range(1, n):
            dp[i][0][0] = max(dp[i - 1][0][0], - prices[i])
            dp[i][1][0] = max(dp[i - 1][1][0], dp[i][0][0] + prices[i])
            for k in range(1, num):
                dp[i][0][k] = max(dp[i - 1][0][k], dp[i][1][k - 1] - prices[i])
                dp[i][1][k] = max(dp[i - 1][1][k], dp[i][0][k] + prices[i])
        return dp[n - 1][1][num - 1]
# if __name__ == "__main__":
