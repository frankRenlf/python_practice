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
        cnt = Counter(nums)
        ret = 1
        for el, val in cnt.items():
            print(el, val)
            ret *= val
        return ret if len(cnt) not in [0, 1, 2] else 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.unequalTriplets([4, 4, 2, 4, 3]))
