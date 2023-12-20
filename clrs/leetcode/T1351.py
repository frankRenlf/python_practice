# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/12/20 17:00 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : easy
"""
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        left = 0
        right = m - 1
        target = 0
        res = 0
        for i in range(n):
            while left < right:
                mid = (left + right) // 2
                if grid[i][mid] >= target:
                    left = mid + 1
                else:
                    right = mid
            res += m - right
            if grid[i][m - 1] >= 0:
                res -= 1
            left = 0
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.countNegatives(grid=[[3, 2], [1, -1]]))
