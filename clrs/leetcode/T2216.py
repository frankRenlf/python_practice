# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/11/21 09:34 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : medium
"""
from typing import List


class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        is_even = True
        for i in range(n - 1):
            if nums[i] == nums[i + 1] and is_even:
                res += 1
            else:
                is_even = not is_even
        return res if (n - res) % 2 == 0 else res + 1
# if __name__ == "__main__":
