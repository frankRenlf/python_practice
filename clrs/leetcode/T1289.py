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
from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for i in range(m)]
        dp[0][:] = grid[0]


if __name__ == "__main__":
    sol = Solution()
    dp = [[0 for _ in range(2)] for i in range(3)]
    grid = [1, 2]
    dp[0][:] = grid
    print(1)
