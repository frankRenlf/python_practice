# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/5/25 10:07 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : easy
"""
from typing import List
from collections import Counter


class Solution:
    def oddString(self, words: List[str]) -> str:
        m = len(words)
        n = len(words[0])
        map = Counter()
        for i in range(m):
            arr = list()
            for j in range(n - 1):
                arr.append(ord(words[i][j + 1]) - ord(words[i][j]))
            s = arr.__str__()
            if map[s] > 0:
                map[s] = -1
            elif map[s] == 0:
                map[s] = i + 1
        return words[max(map.values()) - 1]
