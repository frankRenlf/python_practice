# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/8/4 11:14 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : hard
"""
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        si, sj, n = 0, 0, 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    n += 1
                elif grid[i][j] == 1:
                    n += 1
                    si, sj = i, j

        def dfs(i: int, j: int, n: int) -> int:
            if grid[i][j] == 2:
                if n == 0:
                    return 1
                return 0
            t = grid[i][j]
            grid[i][j] = -1
            res = 0
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < r and 0 <= nj < c and grid[ni][nj] in [0, 2]:
                    res += dfs(ni, nj, n - 1)
            grid[i][j] = t
            return res

        return dfs(si, sj, n)
