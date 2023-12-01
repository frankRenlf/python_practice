# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/12/1 09:17 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        mp = {}
        for i in range(n):
            for j in range(m):
                mp[mat[i][j]] = [i, j]
        rowCnt, colCnt = [0] * n, [0] * m
        for i in range(len(arr)):
            v = mp[arr[i]]
            rowCnt[v[0]] += 1
            if rowCnt[v[0]] == m:
                return i
            colCnt[v[1]] += 1
            if colCnt[v[1]] == n:
                return i
        return -1

# if __name__ == "__main__":
