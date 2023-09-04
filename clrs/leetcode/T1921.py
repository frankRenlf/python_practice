# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/9/3 08:23 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        ans = [dist[i] / speed[i] for i in range(n)]
        ans.sort()
        i = 0
        while i < n and i < ans[i]:
            i += 1
        return i


if __name__ == "__main__":
    sol = Solution()
    print(sol.eliminateMaximum(dist=[1, 1, 2, 3], speed=[1, 1.9, 1, 1]))
