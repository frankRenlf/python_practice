# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/12/14 09:30 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : hard
"""
from typing import List


class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0])
        psum = [[0] * (n + 2) for _ in range(m + 2)]
        diff = [[0] * (n + 2) for _ in range(m + 2)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                psum[i][j] = psum[i - 1][j] + psum[i][j - 1] - psum[i - 1][j - 1] + grid[i - 1][j - 1]

        for i in range(1, m + 2 - stampHeight):
            for j in range(1, n + 2 - stampWidth):
                x = i + stampHeight - 1
                y = j + stampWidth - 1
                if psum[x][y] - psum[x][j - 1] - psum[i - 1][y] + psum[i - 1][j - 1] == 0:
                    diff[i][j] += 1
                    diff[i][y + 1] -= 1
                    diff[x + 1][j] -= 1
                    diff[x + 1][y + 1] += 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1]
                if diff[i][j] == 0 and grid[i - 1][j - 1] == 0:
                    return False
        return True

# if __name__ == "__main__":
