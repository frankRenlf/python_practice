# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/9/12 09:20 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[
        bool]:
        g = [[] for _ in range(numCourses)]
        vi = [False] * numCourses
        isPre = [[False] * numCourses for _ in range(numCourses)]
        for p in prerequisites:
            g[p[0]].append(p[1])

        def dfs(cur):
            if vi[cur]:
                return
            vi[cur] = True
            for ne in g[cur]:
                dfs(ne)
                isPre[cur][ne] = True
                for i in range(numCourses):
                    isPre[cur][i] = isPre[cur][i] | isPre[ne][i]

        for i in range(numCourses):
            dfs(i)
        res = []
        for query in queries:
            res.append(isPre[query[0]][query[1]])
        return res

# if __name__ == "__main__":
