# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2024/1/11 10:28 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""


class Solution:
    def addMinimum(self, word: str) -> int:
        n = len(word)
        d = [0] * (n + 1)
        for i in range(1, n + 1):
            d[i] = d[i - 1] + 2
            if i > 1 and word[i - 1] > word[i - 2]:
                d[i] = d[i - 1] - 1
        return d[n]

# if __name__ == "__main__":
