# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/9/13 09:53 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:

    def __init__(self):
        self.arr = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]
        self.tmp = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]

    def check(self, dic, i, n):
        for el in range(8):
            self.tmp[el][:] = [self.arr[el][0] + dic[i][0], self.arr[el][1] + dic[i][1]]

        return dic[i + 1] in self.tmp

    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if grid[0][0] != 0:
            return False
        dic = {}
        n = len(grid)

        for i in range(n):
            for j in range(n):
                dic[grid[i][j]] = [i, j]
        for i in range(n * n - 1):
            if not self.check(dic, i, n):
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.checkValidGrid(
        [[24, 11, 22, 17, 4],
         [21, 16, 5, 12, 9],
         [6, 23, 10, 3, 18],
         [15, 20, 1, 8, 13],
         [0, 7, 14, 19, 2]]))
