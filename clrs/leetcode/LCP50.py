# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/9/15 09:56 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : easy
"""
from typing import List


class Solution:
    def giveGem(self, gem: List[int], operations: List[List[int]]) -> int:
        for (x, y) in operations:
            given = gem[x] // 2
            gem[y] += given
            gem[x] -= given
        return max(gem) - min(gem)
# if __name__ == "__main__":
