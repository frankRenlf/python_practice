# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/8/10 01:40 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : hard
"""
import sys
from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[sys.maxsize for _ in range(n)] for i in range(m)]
        dp[0][:] = grid[0]
        for i in range(1, n):
            for j in range(m):
                left = sys.maxsize
                right = sys.maxsize
                if j < m - 1:
                    left = min(dp[i - 1][j + 1:n])
                if j > 0:
                    right = min(dp[i - 1][0:j])
                dp[i][j] = min(left, right)
                dp[i][j] += grid[i][j]
        return min(dp[n - 1][0:m])


if __name__ == "__main__":
    sol = Solution()
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(sol.minFallingPathSum(grid))
