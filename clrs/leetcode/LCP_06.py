# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/9/20 09:41 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : easy
"""
import math
from typing import List


class Solution:
    def minCount(self, coins: List[int]) -> int:
        res = 0
        for i in coins:
            res += math.ceil(i / 2)
        return res
# if __name__ == "__main__":
