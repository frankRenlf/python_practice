# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/5/26 10:52 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : middle
"""
from collections import deque
from math import inf
from typing import List
import sys


class Solution:

    def __init__(self):
        self.res = sys.maxsize

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        self.find_path(grid, 0, 0, len(grid), 1)
        return self.res if self.res != sys.maxsize else -1

    def find_path(self, grid, i, j, n, length):
        if self.check(grid, i, j, n):
            if i == n - 1 and j == n - 1:
                self.res = min(self.res, length)
            else:
                grid[i][j] = 1
                length += 1
                self.find_path(grid, i + 1, j, n, length)
                self.find_path(grid, i + 1, j + 1, n, length)
                self.find_path(grid, i, j + 1, n, length)
                self.find_path(grid, i - 1, j + 1, n, length)
                self.find_path(grid, i - 1, j, n, length)
                self.find_path(grid, i - 1, j - 1, n, length)
                self.find_path(grid, i, j - 1, n, length)
                self.find_path(grid, i + 1, j - 1, n, length)
                grid[i][j] = 0
                length -= 1

    def check(self, grid, i, j, n):
        return n > i >= 0 and n > j >= 0 == grid[i][j]

    def shortestPathBinaryMatrix_2(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        n = len(grid)
        dist = [[sys.maxsize] * n for _ in range(n)]
        dist[0][0] = 1
        queue = deque([(0, 0)])
        while queue:
            x, y = queue.popleft()
            if x == y == n - 1:
                return dist[x][y]
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if x + dx < 0 or x + dx >= n or y + dy < 0 or y + dy >= n:  # 越界
                        continue
                    if grid[x + dx][y + dy] == 1 or dist[x + dx][y + dy] <= dist[x][y] + 1:  # 单元格值不为 0 或已被访问
                        continue
                    dist[x + dx][y + dy] = dist[x][y] + 1
                    queue.append((x + dx, y + dy))
        return -1
