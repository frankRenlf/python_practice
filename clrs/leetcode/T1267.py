# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/8/24 10:40 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List
from collections import Counter


class Solution:

    def countServers2(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows, cols = Counter(), Counter()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1):
                    ans += 1

        return ans

    def countServers(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        cnt = 0
        vertical_sum = [[0 for j in range(m)] for i in range(n)]
        horizontal_sum = [[0 for j in range(m)] for i in range(n)]
        vertical_sum[0][:] = grid[0][:]
        for i in range(n):
            horizontal_sum[i][0] = grid[i][0]
        for j in range(m):
            for i in range(1, n):
                vertical_sum[i][j] += vertical_sum[i - 1][j] + grid[i][j]
        for i in range(n):
            for j in range(1, m):
                horizontal_sum[i][j] += horizontal_sum[i][j - 1] + grid[i][j]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    cnt += self.check_around(i, j, n, m, horizontal_sum, vertical_sum)
        return cnt

    def check_around(self, i, j, n, m, horizontal_sum, vertical_sum):
        res = horizontal_sum[i][m - 1] + vertical_sum[n - 1][j]
        return 1 if res > 2 else 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.countServers([[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]))
