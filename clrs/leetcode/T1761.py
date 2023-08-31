# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/8/31 10:31 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : hard
"""
import sys
from collections import defaultdict
from typing import List


class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        # 原图
        g = defaultdict(set)
        # 定向后的图
        h = defaultdict(list)
        degree = [0] * n

        inf = sys.maxsize

        for x, y in edges:
            x, y = x - 1, y - 1
            g[x].add(y)
            g[y].add(x)
            degree[x] += 1
            degree[y] += 1

        for x, y in edges:
            x, y = x - 1, y - 1
            if degree[x] < degree[y] or (degree[x] == degree[y] and x < y):
                h[x].append(y)
            else:
                h[y].append(x)

        ans = inf
        for i in range(n):
            for j in h[i]:
                for k in h[j]:
                    if k in g[i]:
                        ans = min(ans, degree[i] + degree[j] + degree[k] - 6)

        return -1 if ans == inf else ans

# if __name__ == "__main__":
