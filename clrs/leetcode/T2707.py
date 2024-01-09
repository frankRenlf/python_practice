# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2024/1/9 09:51 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        d = [0] * (n + 1)
        for i in range(1, n + 1):
            d[i] = d[i - 1] + 1
            for j in range(0, i):
                if s[j:i] in dictionary:
                    d[i] = min(d[i], d[j])
        return d[n]


if __name__ == "__main__":
    sol = Solution()
    print(sol.minExtraChar(s = "leetscode", dictionary = ["leet","code","leetcode"]))
