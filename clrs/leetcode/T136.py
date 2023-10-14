# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/10/14 09:11 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : easy
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for e in nums:
            res ^= e
        return res
# if __name__ == "__main__":
