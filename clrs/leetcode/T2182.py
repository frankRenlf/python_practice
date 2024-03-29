# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2024/1/13 10:49 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        N = 26
        count = [0] * N
        for c in s:
            count[ord(c) - ord('a')] += 1
        ret = []
        i, j, m = N - 1, N - 2, 0
        while i >= 0 and j >= 0:
            if count[i] == 0:  # 当前字符已经填完，填入后面的字符，重置 m
                m, i = 0, i - 1
            elif m < repeatLimit:  # 当前字符未超过限制
                count[i] -= 1
                ret.append(chr(ord('a') + i))
                m += 1
            elif j >= i or count[j] == 0:  # 当前字符已经超过限制，查找可填入的其他字符
                j -= 1
            else:  # 当前字符已经超过限制，填入其他字符，并且重置 m
                count[j] -= 1
                ret.append(chr(ord('a') + j))
                m = 0
        return ''.join(ret)

# if __name__ == "__main__":
