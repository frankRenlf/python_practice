# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/6/6 08:57 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List
from collections import Counter


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        res, n = 0, len(grid)
        cnt = Counter(tuple(row) for row in grid)
        for j in range(n):
            res += cnt[tuple([grid[i][j] for i in range(n)])]
        return res
