# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/12/5 10:18 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        g = [[] for i in range(len(roads) + 1)]
        for e in roads:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        res = 0

        def dfs(cur, fa):
            nonlocal res
            peopleSum = 1
            for ne in g[cur]:
                if ne != fa:
                    peopleCnt = dfs(ne, cur)
                    peopleSum += peopleCnt
                    res += (peopleCnt + seats - 1) // seats
            return peopleSum

        dfs(0, -1)
        return res


if __name__ == "__main__":
    sol = Solution()
    sol.minimumFuelCost(roads=[[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], seats=2)
    print()
