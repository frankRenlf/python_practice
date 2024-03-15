from functools import cache
from typing import List


class Solution:
    def sellingWood_dp(self, m: int, n: int, prices: List[List[int]]) -> int:
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for h, w, p in prices:
            f[h][w] = p
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                f[i][j] = max(
                    f[i][j],
                    max(
                        (f[i][k] + f[i][j - k] for k in range(1, j // 2 + 1)), default=0
                    ),  # 垂直切割
                    max(
                        (f[k][j] + f[i - k][j] for k in range(1, i // 2 + 1)), default=0
                    ),
                )  # 水平切割
        return f[m][n]

    def sellingWood_mem(self, m: int, n: int, prices: List[List[int]]) -> int:
        value = dict()

        @cache
        def dfs(x: int, y: int) -> int:
            ret = value.get((x, y), 0)

            if x > 1:
                for i in range(1, x // 2 + 1):
                    ret = max(ret, dfs(i, y) + dfs(x - i, y))

            if y > 1:
                for j in range(1, y // 2 + 1):
                    ret = max(ret, dfs(x, j) + dfs(x, y - j))

            return ret

        for h, w, price in prices:
            value[(h, w)] = price

        ans = dfs(m, n)
        dfs.cache_clear()
        return ans
