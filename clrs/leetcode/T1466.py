# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/12/7 09:58 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        ct = [[] for _ in range(n)]
        for edge in connections:
            ct[edge[0]].append([edge[1], 1])
            ct[edge[1]].append([edge[0], 0])

        def dfs(cur, par, ct, connections):
            res = 0
            for e in ct[cur]:
                if e[0] != par:
                    res += e[1] + dfs(e[0], cur, ct, connections)
            return res

        return dfs(0, -1, ct, connections)
# if __name__ == "__main__":
