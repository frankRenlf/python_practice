# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/11/22 10:04 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
import sys
from typing import List


class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mn = len(moveCost)
        dp = [[sys.maxsize for i in range(n)] for j in range(m)]
        for i in range(n):
            dp[0][i] = grid[0][i]
        for i in range(1, m):
            for j in range(n):
                for k in range(n):
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + moveCost[grid[i - 1][k]][j] + grid[i][j])
        return min(dp[m - 1])


if __name__ == "__main__":
    sol = Solution()
    print(sol.minPathCost(grid=[[5, 1, 2], [4, 0, 3]],
                          moveCost=[[12, 10, 15], [20, 23, 8], [21, 7, 1], [8, 1, 13], [9, 10, 25], [5, 3, 2]]))
