# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/6/9 10:00 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : hard
"""
from typing import List


class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> \
            List[List[int]]:
        def dijkstra(adj_matrix: List[List[int]]) -> int:
            # 朴素的 dijkstra 算法
            # adj_matrix 是一个邻接矩阵
            dist = [float("inf")] * n
            used = set()
            dist[source] = 0

            for round in range(n - 1):
                u = -1
                for i in range(n):
                    if i not in used and (u == -1 or dist[i] < dist[u]):
                        u = i
                used.add(u)
                for v in range(n):
                    if v not in used and adj_matrix[u][v] != -1:
                        dist[v] = min(dist[v], dist[u] + adj_matrix[u][v])

            return dist[destination]

        def construct(idx: int) -> List[List[int]]:
            # 需要构造出第 idx 种不同的边权情况，返回一个邻接矩阵
            adj_matrix = [[-1] * n for _ in range(n)]
            for u, v, w in edges:
                if w != -1:
                    adj_matrix[u][v] = adj_matrix[v][u] = w
                else:
                    if idx >= target - 1:
                        adj_matrix[u][v] = adj_matrix[v][u] = target
                        idx -= (target - 1)
                    else:
                        adj_matrix[u][v] = adj_matrix[v][u] = 1 + idx
                        idx = 0
            return adj_matrix

        k = sum(1 for e in edges if e[2] == -1)
        if dijkstra(construct(0)) > target:
            return []
        if dijkstra(construct(k * (target - 1))) < target:
            return []

        left, right, ans = 0, k * (target - 1), 0
        while left <= right:
            mid = (left + right) // 2
            if dijkstra(construct(mid)) >= target:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        for i, e in enumerate(edges):
            if e[2] == -1:
                if ans >= target - 1:
                    edges[i][2] = target
                    ans -= (target - 1)
                else:
                    edges[i][2] = 1 + ans
                    ans = 0

        return edges
