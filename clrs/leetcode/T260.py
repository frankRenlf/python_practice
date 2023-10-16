# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/10/16 10:36 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        pivot = 0
        for num in nums:
            pivot ^= num

        lsb = pivot & (-pivot)
        type1 = type2 = 0
        for num in nums:
            if num & lsb:
                type1 ^= num
            else:
                type2 ^= num

        return [type1, type2]

# if __name__ == "__main__":
