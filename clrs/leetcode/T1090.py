# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/5/23 08:08 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List
from collections import Counter


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        n = len(values)
        idx = list(range(n))
        idx.sort(key=lambda i: -values[i])

        ans = choose = 0
        cnt = Counter()
        for i in range(n):
            label = labels[idx[i]]
            if cnt[label] == useLimit:
                continue
            choose += 1
            ans += values[idx[i]]
            cnt[label] += 1
            if choose == numWanted:
                break
        return ans
