# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/6/13 01:49 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : easy
"""
from typing import List
from collections import Counter


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0
        n = len(nums)
        t = 0
        for _, v in count.items():
            res += t * v * (n - t - v)
            t += v
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.unequalTriplets([4, 4, 2, 4, 3]))
