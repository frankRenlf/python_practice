# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/7/24 00:31 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description :
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelsSet = set(jewels)
        return sum(s in jewelsSet for s in stones)


if __name__ == "__main__":
    s = "ab"
    jewelsSet = set(s)
    stones = "abcdef"
    for s in stones:
        print(s in jewelsSet)
