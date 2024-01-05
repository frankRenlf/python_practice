# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2024/1/5 10:57 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : hard
"""
from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        stack = []
        res = [0] * n
        for i in range(n - 1, -1, -1):
            h = heights[i]
            while stack and h > stack[-1]:
                res[i] += 1
                stack.pop()
            if stack:
                res[i] += 1
            stack.append(h)
        return res

# if __name__ == "__main__":
