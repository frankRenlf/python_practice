from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for i in range(m)]
        ans = 0
        for j in range(1, n):
            for i in range(m):
                pos = [(i - 1, j - 1), (i, j - 1), (i + 1, j - 1)]
                vals = [-1, -1, -1]
                for id, el in enumerate(pos):
                    if (
                        0 <= el[0] < m
                        and 0 <= el[1] < n
                        and grid[i][j] > grid[el[0]][el[1]]
                    ):
                        vals[id] = dp[el[0]][el[1]]
                dp[i][j] = max(vals)
                dp[i][j] += 1 if dp[i][j] != -1 else 0
                ans = max(ans, dp[i][j])
        return ans
