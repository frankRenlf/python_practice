# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/8/2 11:09 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
import sys
from typing import List


class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        n = len(fronts)
        same = set()
        for i in range(n):
            if fronts[i] == backs[i]:
                same.add(fronts[i])
        res = sys.maxsize
        for a in fronts:
            if a < res and a not in same:
                res = a
        for a in backs:
            if a < res and a not in same:
                res = a
        return res if res < 3000 else 0
