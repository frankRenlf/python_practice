# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/6/22 09:03 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    cnt = 0

    def pondSizes(self, land: List[List[int]]) -> List[int]:
        m, n = len(land), len(land[0])
        ret = list()
        for i in range(m):
            for j in range(n):
                if self.check(land, i, j, m, n):
                    self.countArea(land, i, j, m, n)
                    ret.append(self.cnt)
                    self.cnt = 0
        return sorted(ret)

    def check(self, land, i, j, m, n): 
        return not (i < 0 or i >= m or j < 0 or j >= n or land[i][j] > 0)

    def countArea(self, land, i, j, m, n):
        if not self.check(land, i, j, m, n):
            return
        self.cnt += 1
        land[i][j] = 1
        self.countArea(land, i - 1, j, m, n)
        self.countArea(land, i - 1, j + 1, m, n)
        self.countArea(land, i, j + 1, m, n)
        self.countArea(land, i + 1, j + 1, m, n)
        self.countArea(land, i + 1, j, m, n)
        self.countArea(land, i + 1, j - 1, m, n)
        self.countArea(land, i, j - 1, m, n)
        self.countArea(land, i - 1, j - 1, m, n)
