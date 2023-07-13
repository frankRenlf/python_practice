# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/7/13 10:11 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
import sys
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0 for i in range(n)] for j in range(n)]
        for k, v in enumerate(matrix[0]):
            dp[0][k] = v
        for i in range(1, n):
            for j in range(0, n):
                dp[i][j] = self.take_min(dp, i, j, n) + matrix[i][j]
        return min(dp[n - 1])

    def take_min(self, dp, i, j, n):
        res = sys.maxsize
        for k in range(j - 1, j + 2):
            if 0 <= k < n:
                res = min(res, dp[i - 1][k])
        return res
