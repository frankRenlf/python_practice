# 标记 10**5 以内的质数
from math import isqrt
from typing import List


MX = 10**5 + 1
is_prime = [True] * MX
is_prime[1] = False
for i in range(2, isqrt(MX) + 1):
    if is_prime[i]:
        for j in range(i * i, MX, i):
            is_prime[j] = False


class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n + 1)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        def dfs(x: int, fa: int) -> None:
            nodes.append(x)
            for y in g[x]:
                if y != fa and not is_prime[y]:
                    dfs(y, x)

        ans = 0
        size = [0] * (n + 1)
        for x in range(1, n + 1):
            if not is_prime[x]:  # 跳过非质数
                continue
            s = 0
            for y in g[x]:  # 质数 x 把这棵树分成了若干个连通块
                if is_prime[y]:
                    continue
                if size[y] == 0:  # 尚未计算过
                    nodes = []
                    dfs(
                        y, -1
                    )  # 遍历 y 所在连通块，在不经过质数的前提下，统计有多少个非质数
                    for z in nodes:
                        size[z] = len(nodes)
                # 这 size[y] 个非质数与之前遍历到的 s 个非质数，两两之间的路径只包含质数 x
                ans += size[y] * s
                s += size[y]
            ans += s  # 从 x 出发的路径
        return ans
