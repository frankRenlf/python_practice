# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/6/15 09:49 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        count = [0] * (n + 1)
        for i in range(n):
            count[i + 1] = count[i] ^ (1 << (ord(s[i]) - ord('a')))
        res = []
        for l, r, k in queries:
            bits = (count[r + 1] ^ count[l]).bit_count()
            res.append(bits <= k * 2 + 1)
        return res
