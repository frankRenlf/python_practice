from heapq import heappop, heappush
from math import inf
from typing import List
import sys


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 10**9 + 7
        e = [[] for _ in range(n)]
        for x, y, t in roads:
            e[x].append([y, t])
            e[y].append([x, t])
        dis = [0] + [inf] * (n - 1)
        ways = [1] + [0] * (n - 1)

        q = [[0, 0]]
        while q:
            t, u = heappop(q)
            if t > dis[u]:
                continue
            for v, w in e[u]:
                if t + w < dis[v]:
                    dis[v] = t + w
                    ways[v] = ways[u]
                    heappush(q, [t + w, v])
                elif t + w == dis[v]:
                    ways[v] = (ways[u] + ways[v]) % mod
        return ways[-1]


class SolutionPre:
    def __init__(self):
        self.ans = 0
        self.least = sys.maxsize

    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mp = {}
        linked = {}
        for road in roads:
            if road[0] not in mp:
                mp[road[0]] = []
            mp[road[0]].append([road[1], road[2]])
            if road[1] not in mp:
                mp[road[1]] = []
            mp[road[1]].append([road[0], road[2]])

        def dfs(x, f, valsum):
            if valsum > self.least:
                return
            if x == n - 1:
                if valsum == self.least:
                    self.ans += 1
                elif valsum < self.least:
                    self.ans = 1
                    self.least = valsum
                return
            for way in mp[x]:
                if way[0] != f:
                    dfs(way[0], x, valsum + way[1])

        dfs(0, -1, 0)
        return self.ans


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.countPaths(
            n=7,
            roads=[
                [0, 6, 7],
                [0, 1, 2],
                [1, 2, 3],
                [1, 3, 3],
                [6, 3, 3],
                [3, 5, 1],
                [6, 5, 1],
                [2, 5, 1],
                [0, 4, 5],
                [4, 6, 2],
            ],
        )
    )
