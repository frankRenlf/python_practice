# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/10/19 09:05 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List
from collections import Counter


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = Counter([nums[i] * nums[j] for i in range(n) for j in range(i + 1, n)])
        ans = 0
        for _, v in cnt.items():
            ans += v * (v - 1) * 4
        return ans

# if __name__ == "__main__":
