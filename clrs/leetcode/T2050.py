# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/7/28 12:44 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : hard
"""
from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        mx = 0
        prev = [[] for _ in range(n + 1)]
        for x, y in relations:
            prev[y].append(x)

        # @lru_cache(None)
        def dp(i: int) -> int:
            cur = 0
            for p in prev[i]:
                cur = max(cur, dp(p))
            cur += time[i - 1]
            return cur

        for i in range(1, n + 1):
            mx = max(mx, dp(i))
        return mx
