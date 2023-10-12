# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : python_practice 
    @Product : PyCharm
    @createTime : 2023/10/12 09:20 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : easy
"""
from typing import List


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        r = len(nums) - 1
        l = 0
        res = 0
        while l < r:
            res += int(str(nums[l]) + str(nums[r]))
            l += 1
            r -= 1
        return res + nums[l] if l == r else res


if __name__ == "__main__":
    print(int(str(12) + str(34)))
