# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/8/16 09:54 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : easy
"""
from typing import List


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        visit = [False] * n
        i = k
        j = 0
        while not visit[j]:
            visit[j] = True
            j = (j + i) % n
            i += k
        ans = []
        for i in range(n):
            if not visit[i]:
                ans.append(i + 1)
        return ans
