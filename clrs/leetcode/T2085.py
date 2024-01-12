# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2024/1/12 20:30 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : easy
"""
from typing import List
from collections import Counter


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        w1 = Counter(words1)
        w2 = Counter(words2)
        cnt = 0
        for k, v in w1.items():
            if v == 1 and w2[k] == 1:
                cnt += 1
        return cnt
# if __name__ == "__main__":
