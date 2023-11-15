# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/11/15 10:06 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : easy
"""
from typing import List


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        return k * mx + (k - 1) * k // 2
# if __name__ == "__main__":
