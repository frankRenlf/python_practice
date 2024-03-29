# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/12/6 13:58 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : 
"""
from typing import List


class Solution:
    def find(self, uf: List[int], i: int) -> int:
        if uf[i] == i:
            return i
        uf[i] = self.find(uf, uf[i])
        return uf[i]

    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        children = [[] for _ in range(n)]
        for edge in edges:
            children[edge[0]].append(edge[1])
            children[edge[1]].append(edge[0])

        query = [[] for _ in range(n)]
        for trip in trips:
            query[trip[0]].append(trip[1])
            if trip[0] != trip[1]:
                query[trip[1]].append(trip[0])

        uf, visited, diff, parent = [0 for _ in range(n)], [False for _ in range(n)], [0 for _ in range(n)], [0 for _ in
                                                                                                              range(n)]

        def tarjan(node: int, p: int):
            parent[node], uf[node] = p, node
            for child in children[node]:
                if child == p:
                    continue
                tarjan(child, node)
                uf[child] = node
            for node1 in query[node]:
                if node != node1 and not visited[node1]:
                    continue
                lca = self.find(uf, node1)
                diff[node] += 1
                diff[node1] += 1
                diff[lca] -= 1
                if parent[lca] >= 0:
                    diff[parent[lca]] -= 1
            visited[node] = True

        tarjan(0, -1)

        count = [0] * n

        def dfs(node: int, p: int) -> int:
            count[node] = diff[node]
            for child in children[node]:
                if child == p:
                    continue
                count[node] += dfs(child, node)
            return count[node]

        dfs(0, -1)

        def dp(node: int, p: int) -> List[int]:
            res = [
                price[node] * count[node], price[node] * count[node] // 2
            ]
            for child in children[node]:
                if child == p:
                    continue
                [x, y] = dp(child, node)
                # node 没有减半，因此可以取子树的两种情况的最小值
                # node 减半，只能取子树没有减半的情况
                res[0], res[1] = res[0] + min(x, y), res[1] + x
            return res

        return min(dp(0, -1))

# if __name__ == "__main__":
