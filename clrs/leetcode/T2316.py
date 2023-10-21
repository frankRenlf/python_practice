# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/10/21 09:25 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        visited = [False] * n

        def dfs(x: int) -> int:
            visited[x] = True
            count = 1
            for y in graph[x]:
                if not visited[y]:
                    count += dfs(y)
            return count

        res = 0
        for i in range(n):
            if not visited[i]:
                count = dfs(i)
                res += count * (n - count)
        return res // 2

# if __name__ == "__main__":
