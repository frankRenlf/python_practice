# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/11/14 10:52 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
import sys
from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        ans = (sys.maxsize, -1)
        mp = [[sys.maxsize] * n for _ in range(n)]

        for fr, to, weight in edges:
            mp[fr][to], mp[to][fr] = weight, weight
        for k in range(n):
            mp[k][k] = 0
            for i in range(n):
                for j in range(n):
                    mp[i][j] = min(mp[i][j], mp[i][k] + mp[k][j])
        for i in range(n):
            cnt = sum(mp[i][j] <= distanceThreshold for j in range(n))
            if cnt <= ans[0]:
                ans = (cnt, i)
        return ans[1]

# if __name__ == "__main__":
