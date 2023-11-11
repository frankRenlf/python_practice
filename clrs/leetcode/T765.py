# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/11/11 10:21 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : hard
"""
from typing import List


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        def find(x: int) -> int:
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        n = len(row) >> 1
        p = list(range(n))
        for i in range(0, len(row), 2):
            a, b = row[i] >> 1, row[i + 1] >> 1
            p[find(a)] = find(b)
        return n - sum(i == find(i) for i in range(n))

# if __name__ == "__main__":
