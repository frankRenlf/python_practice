# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/8/22 00:39 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


# if __name__ == "__main__":
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        res, l = 0, 0
        while l < len(seats) and seats[l] == 0:
            l += 1
        res = max(res, l)
        while l < len(seats):
            r = l + 1
            while r < len(seats) and seats[r] == 0:
                r += 1
            if r == len(seats):
                res = max(res, r - l - 1)
            else:
                res = max(res, (r - l) // 2)
            l = r
        return res
