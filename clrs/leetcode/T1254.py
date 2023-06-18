# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/6/18 09:19 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        cnt = 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            self.remove_is(grid, i, 0, m, n)
            self.remove_is(grid, i, n - 1, m, n)
            for j in range(n):
                self.remove_is(grid, 0, j, m, n)
                self.remove_is(grid, m - 1, j, m, n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    cnt += 1
                    self.remove_is(grid, i, j, m, n)
        return cnt

    def remove_is(self, grid, i, j, m, n):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 1:
            return
        grid[i][j] = 1
        self.remove_is(grid, i - 1, j, m, n)
        self.remove_is(grid, i, j + 1, m, n)
        self.remove_is(grid, i + 1, j, m, n)
        self.remove_is(grid, i, j - 1, m, n)


if __name__ == '__main__':
    sol = Solution()
    print(sol.closedIsland([[1, 1, 1, 1, 1, 1, 1],
                            [1, 0, 0, 0, 0, 0, 1],
                            [1, 0, 1, 1, 1, 0, 1],
                            [1, 0, 1, 0, 1, 0, 1],
                            [1, 0, 1, 1, 1, 0, 1],
                            [1, 0, 0, 0, 0, 0, 1],
                            [1, 1, 1, 1, 1, 1, 1]]))
