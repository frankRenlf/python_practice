# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/7/18 10:42 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : hard
"""

from heapq import heappush, heappop
from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n, m = len(intervals), len(queries)
        intervals.sort()
        queries = sorted([x, i] for i, x in enumerate(queries))
        ans = [-1] * m
        pq = []
        i = 0
        for x, j in queries:
            while i < n and intervals[i][0] <= x:
                a, b = intervals[i]
                heappush(pq, (b - a + 1, b))
                i += 1
            while pq and pq[0][1] < x:
                heappop(pq)
            if pq:
                ans[j] = pq[0][0]
        return ans


if __name__ == "__main__":
    queries = [1, 2, 3]
    arr = [[x, i] for i, x in enumerate(queries)]
    brr = sorted([x, i] for i, x in enumerate(queries))
    crr = sorted((x, i) for i, x in enumerate(queries))
    drr = ([x, i] for i, x in enumerate(queries))
    print(arr, type(arr))
    print(brr, type(brr))
    print(crr, type(crr))
