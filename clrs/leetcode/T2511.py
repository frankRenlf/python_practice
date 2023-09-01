# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/9/2 00:35 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : easy
"""
from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        cnt = 0
        n = len(forts)

        def move(forts, i, n, add):
            if i < 0 or i >= n or forts[i] != 0:
                return 0
            forts[i] = -1
            add += move(forts, i - 1, n, 0) + move(forts, i + 1, n, 0) + 1
            forts[i] = 0
            return add

        for i in range(n):
            if forts[i] == 1:
                cnt = max(move(forts, i - 1, n, 0), move(forts, i + 1, n, 0), cnt)

        return cnt


if __name__ == "__main__":
    sol = Solution()
    print(sol.captureForts([1, 0, 0, -1, 1, 0, 0, 0, 1]))
