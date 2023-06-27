# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/6/27 08:53 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
import sys
from typing import List


class Solution:
    def maximumSum(self, arr: List[int]) -> bool:
        n = len(arr)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = arr[0]
        dp[0][1] = 0
        res = dp[0][0]
        for i in range(1, n):
            dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + arr[i])
            dp[i][0] = max(dp[i - 1][0] + arr[i], arr[i])
            res = max(res, dp[i][0], dp[i][1])
        return res
