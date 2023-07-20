# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/7/19 02:03 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        px, py, d = 0, 0, 1
        obs_map = set([tuple(i) for i in obstacles])
        res = 0
        for c in commands:
            if c < 0:
                d += 1 if c == -1 else -1
                d %= 4
            else:
                for i in range(c):
                    if tuple([px + dirs[d][0], py + dirs[d][1]]) in obs_map:
                        break
                    px, py = px + dirs[d][0], py + dirs[d][1]
                    res = max(res, px * px + py * py)
        return res
